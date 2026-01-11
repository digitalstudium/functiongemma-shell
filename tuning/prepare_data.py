import json

from common import DEFAULT_SYSTEM_MSG, PATH_TEST, PATH_TRAIN, TOOLS
from data_raw import sample_dataset
from datasets import Dataset


def format_sample(sample):
    """Превращает сырой пример в формат чата для FunctionGemma"""
    return {
        "messages": [
            {"role": "developer", "content": DEFAULT_SYSTEM_MSG},
            {"role": "user", "content": sample["user_content"]},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "type": "function",
                        "function": {
                            "name": sample["tool_name"],
                            "arguments": json.loads(sample["tool_arguments"]),
                        },
                    }
                ],
            },
        ],
        "tools": TOOLS,
    }


def main():
    print(">>> 1. Загрузка сырых данных...")
    dataset = Dataset.from_list(sample_dataset)

    print(">>> 2. Форматирование данных...")
    dataset = dataset.map(format_sample, remove_columns=dataset.features, batched=False)

    print(">>> 3. Разделение на train/test (50/50)...")
    # seed=42 критичен для воспроизводимости
    split_dataset = dataset.train_test_split(test_size=0.5, shuffle=True, seed=42)

    print(f">>> 4. Сохранение данных на диск...")
    print(f"    Train -> {PATH_TRAIN}")
    split_dataset["train"].save_to_disk(PATH_TRAIN)

    print(f"    Test  -> {PATH_TEST}")
    split_dataset["test"].save_to_disk(PATH_TEST)

    print(">>> Готово. Можно запускать train.py или eval.py")


if __name__ == "__main__":
    main()
