# Interview Q&A

**1️⃣ What is DistilBERT?**
A distilled version of BERT — smaller, faster, but with nearly the same performance.

**2️⃣ Why use IMDB dataset?**
It's a classic benchmark for binary sentiment classification.

**3️⃣ What library is used for training?**
HuggingFace Transformers + Datasets + PyTorch.

**4️⃣ What does tokenizer do?**
Converts text into numerical tokens understandable by the model.

**5️⃣ Why save model with `save_pretrained()`?**
It stores model architecture + weights + tokenizer files for easy reload.

**6️⃣ What is softmax used for?**
To convert logits into probability scores.

**7️⃣ How do you prevent model duplication?**
Using a flag file `save_complete.flag` in the results folder.

**8️⃣ What is the /predict endpoint for?**
To take user input and return sentiment prediction via Flask API.

**9️⃣ Why use Flask here?**
It’s lightweight and perfect for serving ML inference APIs.

**🔟 How to deploy this API to production?**
Containerize with Docker + Gunicorn, deploy on cloud (AWS/Azure/GCP).
