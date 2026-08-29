import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

MODEL_NAME = "WineQualityModel"

client = MlflowClient()

staging_version = client.get_model_version_by_alias(
    MODEL_NAME,
    "staging"
)

client.set_registered_model_alias(
    MODEL_NAME,
    "champion",
    staging_version.version
)

print("Model promoted successfully!")
print("Model:", MODEL_NAME)
print("Version:", staging_version.version)
print("Alias: champion")
