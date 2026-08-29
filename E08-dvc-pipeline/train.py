import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("train.csv")

X = train.drop("passed", axis=1)
y = train["passed"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model training completed.")
