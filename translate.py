from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "fine_tuned_cg_model"
TOKENIZER_DIR = BASE_DIR / "fine_tuned_cg_tokenizer"

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Loading VaaniAI translation model on {device}...")
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR).to(device)
    model.eval()
    print("Ready. Enter Chhattisgarhi text; type q to quit.")
    while True:
        text = input("Chhattisgarhi> ").strip()
        if text.lower() in {"q", "quit", "exit"}:
            break
        if not text:
            continue
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256).to(device)
        with torch.inference_mode():
            output = model.generate(**inputs, max_length=256, num_beams=5)
        print("English>", tokenizer.decode(output[0], skip_special_tokens=True))

if __name__ == "__main__":
    main()
