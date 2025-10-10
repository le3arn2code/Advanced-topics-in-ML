# Auto-stop safeguard for SHAP
import os, sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
LOCK="/tmp/lab10_shap.lock"
if os.path.exists(LOCK):
    print("SHAP already executed. Exit.")
    sys.exit(0)
open(LOCK, "w").write("1")

import shap, tensorflow as tf

# Load model & data
model = tf.keras.models.load_model("models/adult_tf.keras")
data = np.load("data/splits.npz")
X_train, X_test = data["X_train"], data["X_test"]

# Keep things tiny for t3.medium
bg = X_train[:200]   # background for expectations
xt = X_test[:50]     # explain only 50 rows

# New SHAP API: let it pick best explainer (usually Gradient for TF)
explainer = shap.Explainer(model, shap.maskers.Independent(bg))
shap_values = explainer(xt)

# 1) Global importance (bar)
plt.figure()
shap.plots.bar(shap_values, show=False)
plt.tight_layout(); plt.savefig("screenshots/shap_summary_bar.png", dpi=140)

# 2) Beeswarm
plt.figure()
shap.plots.beeswarm(shap_values, show=False, max_display=12)
plt.tight_layout(); plt.savefig("screenshots/shap_beeswarm.png", dpi=140)

# 3) One force plot via matplotlib (index 0)
try:
    plt.figure()
    shap.plots.force(shap_values[0], matplotlib=True, show=False)
    plt.tight_layout(); plt.savefig("screenshots/shap_force_idx0.png", dpi=140)
except Exception as e:
    open("screenshots/force_plot_error.txt","w").write(str(e))

print("Saved SHAP plots to screenshots/.")
os.remove(LOCK)
