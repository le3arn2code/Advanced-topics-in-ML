# Auto-stop safeguard for fairness
import os, sys, json, numpy as np
LOCK="/tmp/lab10_fairness.lock"
if os.path.exists(LOCK):
    print("Fairness already executed. Exit.")
    sys.exit(0)
open(LOCK, "w").write("1")

import tensorflow as tf
from sklearn.metrics import confusion_matrix

data = np.load("data/splits.npz")
X_test, y_test, sex_test = data["X_test"], data["y_test"], data["sex_test"]

model = tf.keras.models.load_model("models/adult_tf.keras")
proba = model.predict(X_test, verbose=0).ravel()
y_pred = (proba > 0.5).astype(int)

# Assume sex encoding: 0/1 (depends on LabelEncoder), compute per-group
groups = {}
for g in np.unique(sex_test):
    mask = sex_test == g
    yt, yp = y_test[mask], y_pred[mask]
    tn, fp, fn, tp = confusion_matrix(yt, yp, labels=[0,1]).ravel()
    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    pos_rate = yp.mean() if len(yp)>0 else 0.0
    groups[int(g)] = {"TPR": float(tpr), "FPR": float(fpr), "PositiveRate": float(pos_rate), "Count": int(mask.sum())}

# Choose two groups if available: min code as A, max code as B
keys = sorted(groups.keys())
fair = {"groups": groups, "notes": "sex codes originate from LabelEncoder on 'sex' column"}
if len(keys) >= 2:
    a, b = keys[0], keys[1]
    # Disparate Impact Ratio: PR_B / PR_A
    dir_val = (groups[b]["PositiveRate"] / groups[a]["PositiveRate"]) if groups[a]["PositiveRate"]>0 else None
    # Equal Opportunity Difference: TPR_B - TPR_A
    eod = groups[b]["TPR"] - groups[a]["TPR"]
    fair["disparate_impact_ratio"] = dir_val
    fair["equal_opportunity_diff"] = eod

os.makedirs("screenshots", exist_ok=True)
with open("screenshots/fairness_metrics.json","w") as f:
    json.dump(fair, f, indent=2)
with open("screenshots/fairness_metrics.md","w") as f:
    f.write("# Fairness Metrics (sex)\n\n")
    for k,v in groups.items():
        f.write(f"- sex_code={k}: TPR={v['TPR']:.3f}, FPR={v['FPR']:.3f}, PosRate={v['PositiveRate']:.3f}, N={v['Count']}\n")
    if "disparate_impact_ratio" in fair and fair["disparate_impact_ratio"] is not None:
        f.write(f"\n**Disparate Impact Ratio** (B/A): {fair['disparate_impact_ratio']:.3f}\n")
        f.write(f"**Equal Opportunity Difference** (B-A, TPR): {fair['equal_opportunity_diff']:.3f}\n")

print("Saved fairness metrics to screenshots/.")
os.remove(LOCK)
