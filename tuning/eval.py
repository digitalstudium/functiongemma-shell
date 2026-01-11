import json
import re
from typing import Dict, List, Tuple

from common import PATH_TEST, TOOLS
from datasets import load_from_disk
from transformers import AutoModelForCausalLM, AutoTokenizer

# ======================================================
# Укажите модель здесь (HF repo или локальный путь)
# ======================================================
# MODEL_ID = "functiongemma-270m-it-shell"  # local tuned
# MODEL_ID = "digitalstudium/functiongemma-270m-it-shell" # remote tuned
MODEL_ID = "google/functiongemma-270m-it"  # original
# ======================================================


def parse_functiongemma_output(text: str) -> List[Tuple[str, Dict]]:
    """
    Парсит вывод FunctionGemma с <escape> вместо кавычек.
    Возвращает список (name, args_dict)
    """
    calls = []

    # Ищем все блоки <start_function_call>...</end_function_call>
    blocks = re.split(r"<start_function_call>", text)
    for block in blocks[1:]:
        end = block.find("<end_function_call>")
        if end != -1:
            block = block[:end]

        # Ищем call:name
        m = re.search(r"call:([a-zA-Z0-9_]+)", block)
        if not m:
            continue
        name = m.group(1)

        # Берём всё после имени функции
        args_part = block[m.end() :].strip()

        # Заменяем <escape> на кавычки
        args_part = args_part.replace("<escape>", '"')

        # Убираем лишние пробелы между ключом и значением
        args_part = re.sub(r"([{\[,])\s+", r"\1", args_part)
        args_part = re.sub(r"\s+([}\],])", r"\1", args_part)

        # Пробуем распарсить как JSON
        try:
            args = json.loads(args_part)
        except Exception:
            # Если не получилось — попробуем вручную собрать dict
            args = {}
            # Пример: {url:"https://ya.ru"}
            matches = re.findall(r'([a-zA-Z0-9_]+):"([^"]*)"', args_part)
            for k, v in matches:
                args[k] = v

        calls.append((name, args))

    return calls


def normalize_args(args: Dict) -> Dict:
    """Приводит аргументы к единому виду для сравнения"""
    if args is None:
        return {}
    normalized = {}
    for k, v in args.items():
        if v is None:
            normalized[k] = None
        elif isinstance(v, str):
            # Убираем https:// если есть, и www.
            cleaned = v.strip()
            if k == "url":
                cleaned = (
                    cleaned.replace("https://", "").replace("http://", "").strip("/")
                )
                if cleaned.startswith("www."):
                    cleaned = cleaned[4:]
            normalized[k] = cleaned
        else:
            normalized[k] = v
    return normalized


def check_success_rate():
    print(f">>> Loading model: {MODEL_ID}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype="auto",
        device_map="auto",
        attn_implementation="eager",
    )

    print(f">>> Loading test dataset from: {PATH_TEST}")
    test_dataset = load_from_disk(PATH_TEST)

    success = 0
    total = len(test_dataset)

    for idx, item in enumerate(test_dataset):
        messages = item["messages"][:2]
        expected = item["messages"][2]["tool_calls"][0]["function"]
        expected_name = expected["name"]
        expected_args_raw = expected["arguments"]

        # Ожидаемые аргументы (в вашем датасете есть лишние поля directory/url)
        expected_args = {k: v for k, v in expected_args_raw.items() if v is not None}
        expected_args_norm = normalize_args(expected_args)

        inputs = tokenizer.apply_chat_template(
            messages,
            tools=TOOLS,
            add_generation_prompt=True,
            return_dict=True,
            return_tensors="pt",
        )

        out = model.generate(
            **inputs.to(model.device),
            pad_token_id=tokenizer.eos_token_id,
            max_new_tokens=128,
        )

        generated = tokenizer.decode(
            out[0][len(inputs["input_ids"][0]) :],
            skip_special_tokens=False,
        )

        calls = parse_functiongemma_output(generated)

        is_correct = False
        reason = ""

        if calls:
            pred_name, pred_args = calls[0]
            pred_args_norm = normalize_args(pred_args)

            name_ok = pred_name == expected_name
            args_ok = pred_args_norm == expected_args_norm

            if name_ok and args_ok:
                is_correct = True
            else:
                reason = f"name_ok={name_ok}, args_ok={args_ok}"
        else:
            reason = "no call found"

        if is_correct:
            success += 1

        print(f"\n[{idx + 1}/{total}]")
        print(f"  Q: {messages[1]['content']}")
        print(f"  Expected: {expected_name} {expected_args_norm}")
        print(f"  Got:      {calls[0] if calls else 'None'}")
        print(f"  Result: {'OK' if is_correct else 'FAIL'} | {reason}")

    print("\n" + "=" * 60)
    print(f"FINAL RESULT: {success}/{total} ({success / total * 100:.2f}%)")
    print("=" * 60)


if __name__ == "__main__":
    check_success_rate()
