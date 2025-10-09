# Lab 08 – Advanced NLP with DistilBERT: Training + Flask Inference API

This lab demonstrates fine-tuning the DistilBERT transformer model for sentiment analysis using the IMDB dataset, followed by deploying a Flask API for real-time inference.

## Objectives
1. Fine-tune DistilBERT on IMDB dataset.
2. Save the trained model for later use.
3. Deploy a simple Flask API to serve predictions.

## Steps Summary
```bash
# 1️⃣ Create environment
python3 -m venv nlp_env && source nlp_env/bin/activate
pip install torch transformers datasets flask

# 2️⃣ Train model
python3 code/train_bert_imdb.py | tee screenshots/train_output.txt

# 3️⃣ Save trained model
python3 code/save_trained_model.py

# 4️⃣ Run Flask API
python3 code/app.py
```

## Test API
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"text": "This movie was great!"}'
```

## Results
Model and tokenizer saved under `results/` folder.
