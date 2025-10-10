# Auto-stop safeguard for training
import os, sys, json, joblib, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

LOCK="/tmp/lab10_train.lock"
if os.path.exists(LOCK):
    print("Training already executed. Exit.")
    sys.exit(0)
Path(LOCK).write_text(str(os.getpid()))

import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, f1_score

os.makedirs("screenshots", exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Lighter TF logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# 1) Load Adult dataset (UCI)
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
cols = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
        'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']

df = pd.read_csv(URL, names=cols, sep=r",\s*", engine="python", na_values="?")
df.dropna(inplace=True)

# Convert target to binary
df["income"] = df["income"].str.strip().apply(lambda s: 1 if ">50K" in s else 0)

# Keep light: select subset of rows (optional for t3.medium)
df = df.sample(n=min(25000, len(df)), random_state=42)

# Split features/target
y = df["income"].values
X_df = df.drop(columns=["income"]).copy()

# Categorical and numeric columns
cat_cols = ['workclass','education','marital-status','occupation','relationship','race','sex','native-country']
num_cols = [c for c in X_df.columns if c not in cat_cols]

# Encode categoricals
encoders = {}
for c in cat_cols:
    le = LabelEncoder()
    X_df[c] = le.fit_transform(X_df[c].astype(str))
    encoders[c] = {"classes_": le.classes_.tolist()}

# Save encoded 'sex' separately for fairness later
sex_encoded = X_df["sex"].values.copy()

# Scale numeric
scaler = StandardScaler()
X_df[num_cols] = scaler.fit_transform(X_df[num_cols])

X = X_df.values

X_train, X_test, y_train, y_test, sex_train, sex_test = train_test_split(
    X, y, sex_encoded, test_size=0.2, random_state=42, stratify=y
)

# 2) Define a tiny dense model
tf.random.set_seed(42)
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# 3) Train lightly
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=4, batch_size=64, verbose=1
)

# 4) Evaluate & save metrics
pred = (model.predict(X_test, verbose=0) > 0.5).astype(int).ravel()
acc = accuracy_score(y_test, pred)
f1 = f1_score(y_test, pred)

with open("screenshots/metrics.txt", "w") as f:
    f.write(f"Accuracy: {acc:.4f}\nF1: {f1:.4f}\n")

# Plot training curves
plt.figure()
plt.plot(history.history["loss"], label="loss")
plt.plot(history.history["val_loss"], label="val_loss")
plt.legend(); plt.title("Training Loss"); plt.xlabel("epoch"); plt.ylabel("loss")
plt.tight_layout(); plt.savefig("screenshots/training_loss.png", dpi=140)

plt.figure()
plt.plot(history.history["accuracy"], label="acc")
plt.plot(history.history["val_accuracy"], label="val_acc")
plt.legend(); plt.title("Training Accuracy"); plt.xlabel("epoch"); plt.ylabel("acc")
plt.tight_layout(); plt.savefig("screenshots/training_acc.png", dpi=140)

# Save model and preprocessing
model.save("models/adult_tf.keras")
joblib.dump(scaler, "models/scaler.joblib")
with open("models/encoders.json", "w") as f:
    json.dump(encoders, f)

# Save arrays for reuse
np.savez_compressed("data/splits.npz",
    X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, sex_test=sex_test
)

print(f"Saved model and artifacts. Acc={acc:.4f}, F1={f1:.4f}")
os.remove(LOCK)
