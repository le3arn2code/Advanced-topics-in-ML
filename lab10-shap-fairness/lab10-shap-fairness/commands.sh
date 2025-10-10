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
