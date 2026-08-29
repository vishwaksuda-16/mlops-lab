import mlflow
from mlflow import MlflowClient

RUN_ID = "99d3fa7845e04803bbe65166de1e1399"

MODEL_NAME = "WineQualityModel"

mlflow.set_tracking_uri("http://127.0.0.1:5000")

model_uri = f"runs:/{RUN_ID}/model"

print("Registering model...")
print("Run ID:", RUN_ID)

result = mlflow.register_model(
    model_uri=model_uri,
    name=MODEL_NAME
)

print("\nModel registered successfully!")
print("Model Name:", result.name)
print("Version:", result.version)

client = MlflowClient()

client.update_model_version(
    name=MODEL_NAME,
    version=result.version,
    description="Logistic Regression model selected from E07"
)

client.set_model_version_tag(
    name=MODEL_NAME,
    version=result.version,
    key="dataset",
    value="wine-quality-v1"
)

print("Description and tags added.")
