# Lab 10 – Model Fairness & Explainability with SHAP (CPU‑only, t3.medium)

## 🎯 Objective
- Train a **lightweight** TensorFlow model on the **Adult Income** dataset.
- Use **SHAP** to explain predictions (global + local).
- Evaluate **fairness** with simple metrics across **gender (sex)**.
- Save all visualizations to the `screenshots/` folder.

> This lab is optimized for **t3.medium (2 vCPU / 4 GB RAM)**. No system upgrades. No virtualenvs. Use `--break-system-packages`.

---

## 📦 Step 0 – Folder
```bash
mkdir -p lab10-shap-fairness/{code,models,data,screenshots}
cd lab10-shap-fairness
```

---

## 🧰 Step 1 – Install Dependencies (no upgrades, break-system method)

**Filename**
```bash
nano commands.sh
```

**Code**
```bash
#!/bin/bash
# Lab 10 – SHAP Fairness (CPU-only) — commands.sh
# Auto-stop safeguard: prevent duplicate executions
LOCK="/tmp/lab10_commands.lock"
if [ -f "$LOCK" ]; then
  echo "Lab 10 already running. Exit."
  exit 0
fi
echo $$ > "$LOCK"

# 1) Python deps (CPU-friendly). No apt upgrades; use --break-system-packages
pip install --break-system-packages --no-cache-dir   shap==0.46.0 tensorflow==2.16.1 scikit-learn==1.5.2   pandas==2.2.3 matplotlib==3.10.0 joblib==1.4.2

# 2) Run training (lightweight)
python3 code/train_light_tf.py

# 3) Run SHAP explainability (small slices)
python3 code/explain_with_shap.py

# 4) Run fairness metrics
python3 code/fairness_metrics.py

echo "✅ Lab 10 complete. Artifacts saved under screenshots/, models/, data/"
rm -f "$LOCK"
```

**Make runnable**
```bash
chmod +x commands.sh
```

---

## 🧪 Step 2 – Training (Tiny TF model, saves artifacts)

**Filename**
```bash
nano code/train_light_tf.py
```

Paste the code from this repository file.

---

## 🔎 Step 3 – SHAP Explainability (small background & test sample)

**Filename**
```bash
nano code/explain_with_shap.py
```

Paste the code from this repository file.

---

## ⚖️ Step 4 – Fairness Metrics (sex groups)

**Filename**
```bash
nano code/fairness_metrics.py
```

Paste the code from this repository file.

---

## 🧯 Step 5 – Troubleshooting
See `troubleshooting.md`

## 💬 Step 6 – Interview Q&A
See `interview_qna.md`

## 🧠 Step 7 – Layman Explanation
See `layman_explanation.md`
