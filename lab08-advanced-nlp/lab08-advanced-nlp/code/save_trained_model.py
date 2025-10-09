from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import os, sys

MODEL_NAME = "distilbert-base-uncased"
SAVE_PATH = "results"
FLAG_FILE = os.path.join(SAVE_PATH, "save_complete.flag")

if os.path.exists(FLAG_FILE):
    print("✅ Model already saved previously. Skipping duplicate run.")
    sys.exit(0)

print("🔍 Downloading model and tokenizer...")
model = DistilBertForSequenceClassification.from_pretrained(MODEL_NAME)
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_NAME)

os.makedirs(SAVE_PATH, exist_ok=True)
model.save_pretrained(SAVE_PATH)
tokenizer.save_pretrained(SAVE_PATH)

with open(FLAG_FILE, "w") as f:
    f.write("Model saved successfully.\n")

print("✅ Model and tokenizer saved to:", SAVE_PATH)
