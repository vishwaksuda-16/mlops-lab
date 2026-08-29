import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

MODEL_NAME = "WineQualityModel"
ALIAS = "staging"
MIN_ACCURACY = 0.90

client = MlflowClient()

# Get the model version using the staging alias
model_version = client.get_model_version_by_alias(
    MODEL_NAME,
    ALIAS
)

print("Model:", MODEL_NAME)
print("Version:", model_version.version)
print("Alias:", ALIAS)

# Get the original training run
run = client.get_run(model_version.run_id)

accuracy = run.data.metrics["accuracy"]

print(f"Accuracy: {accuracy:.4f}")
print(f"Required: {MIN_ACCURACY:.2f}")

if accuracy >= MIN_ACCURACY:
    print("Validation PASSED")
else:
    print("Validation FAILED")
    raise SystemExit(1)
