import pandas as pd
import pickle
import json

from sklearn.metrics import accuracy_score

test = pd.read_csv("test.csv")

X = test.drop("passed", axis=1)
y = test["passed"]

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

metrics = {
    "accuracy": round(float(accuracy), 4)
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print(f"Model accuracy: {accuracy:.4f}")
print("Metrics saved to metrics.json")
