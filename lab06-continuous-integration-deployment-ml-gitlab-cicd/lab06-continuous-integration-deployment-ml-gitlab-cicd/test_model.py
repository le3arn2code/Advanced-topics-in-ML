from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import joblib

X, y = load_iris(return_X_y=True)
model = joblib.load('iris_model.pkl')
pred = model.predict(X)
print("Accuracy:", accuracy_score(y, pred))
