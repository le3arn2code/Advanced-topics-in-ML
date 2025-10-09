from flask import Flask, request, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch, os

app = Flask(__name__)
MODEL_DIR = "results"

if not os.path.exists(MODEL_DIR):
    raise FileNotFoundError("Model directory not found. Run save_trained_model.py first.")

tokenizer = DistilBertTokenizer.from_pretrained(MODEL_DIR)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        label = "Positive" if pred == 1 else "Negative"

    return jsonify({"text": text, "sentiment": label, "confidence": float(probs[0][pred])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
