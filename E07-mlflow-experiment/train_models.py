import mlflow
import mlflow.sklearn
import mlflow.xgboost

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from xgboost import XGBClassifier


# Load dataset
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# MLflow configuration
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("E07-Multi-Model-Experiment")


def train_and_log(model, model_name):
    with mlflow.start_run(run_name=model_name):

        # Train
        model.fit(X_train, y_train)

        # Predict
        predictions = model.predict(X_test)

        # Metrics
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        # Log parameters
        mlflow.log_param("model", model_name)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        # Confusion matrix
        cm = confusion_matrix(y_test, predictions)

        plt.figure()
        plt.imshow(cm)
        plt.title(f"{model_name} - Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.colorbar()

        for i in range(len(cm)):
            for j in range(len(cm[i])):
                plt.text(j, i, cm[i][j], ha="center", va="center")

        plt.tight_layout()

        artifact_name = f"{model_name}_confusion_matrix.png"
        plt.savefig(artifact_name)
        plt.close()

        mlflow.log_artifact(artifact_name)

        # Log model
        if model_name == "XGBoost":
            mlflow.xgboost.log_model(model, "model")
        else:
            mlflow.sklearn.log_model(model, "model")

        print(f"\n{model_name}")
        print(f"Accuracy : {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall   : {recall:.4f}")
        print(f"F1 Score : {f1:.4f}")


# Model 1 - Logistic Regression
train_and_log(
    LogisticRegression(max_iter=2000),
    "Logistic Regression"
)

# Model 2 - Random Forest
train_and_log(
    RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "Random Forest"
)

# Model 3 - XGBoost
train_and_log(
    XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss"
    ),
    "XGBoost"
)

print("\nAll three models trained and logged successfully!")
