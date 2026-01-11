import torch
from common import PATH_TEST, PATH_TRAIN
from datasets import load_from_disk
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTConfig, SFTTrainer

# ====== настройки ======
BASE_MODEL = "google/functiongemma-270m-it"
MY_MODEL_NAME = OUTPUT_DIR = "functiongemma-270m-it-shell"
LEARNING_RATE = 5e-5
HUB_MODEL_ID = "digitalstudium/" + MY_MODEL_NAME
# =======================


def train():
    print(
        f">>> Loading prepared datasets:\n  train: {PATH_TRAIN}\n  test:  {PATH_TEST}"
    )
    train_dataset = load_from_disk(PATH_TRAIN)
    eval_dataset = load_from_disk(PATH_TEST)

    print(">>> Loading model/tokenizer...")
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype="auto",  # ВАЖНО: используйте torch_dtype, не fp16 вручную
        device_map="auto",
        attn_implementation="eager",
    )
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

    # Автоматически выбираем режим точности по dtype модели
    torch_dtype = model.dtype
    use_fp16 = torch_dtype == torch.float16
    use_bf16 = torch_dtype == torch.bfloat16

    print(f">>> Model dtype: {torch_dtype} | fp16={use_fp16} bf16={use_bf16}")

    args = SFTConfig(
        output_dir=OUTPUT_DIR,  # directory to save and repository id
        max_length=512,  # max sequence length for model and packing of the dataset
        packing=False,  # Groups multiple samples in the dataset into a single sequence
        num_train_epochs=8,  # number of training epochs
        per_device_train_batch_size=2,  # batch size per device during training
        gradient_checkpointing=False,  # Caching is incompatible with gradient checkpointing
        optim="adamw_torch_fused",  # use fused adamw optimizer
        logging_steps=1,  # log every step
        # save_strategy="epoch",                  # save checkpoint every epoch
        eval_strategy="epoch",  # evaluate checkpoint every epoch
        learning_rate=LEARNING_RATE,  # learning rate
        fp16=True if torch_dtype == torch.float16 else False,  # use float16 precision
        bf16=True if torch_dtype == torch.bfloat16 else False,  # use bfloat16 precision
        lr_scheduler_type="constant",  # use constant learning rate scheduler
        report_to="tensorboard",  # report metrics to tensorboard
        per_device_eval_batch_size=2,
        eval_accumulation_steps=4,  # helps reduce GPU peak during eval
        hub_model_id=HUB_MODEL_ID,
        push_to_hub=True,  # push model to hub
    )

    trainer = SFTTrainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        processing_class=tokenizer,
    )

    print(">>> Training...")
    trainer.train()
    trainer.save_model()
    print(">>> Done.")


if __name__ == "__main__":
    train()
