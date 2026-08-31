import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Iris ML Prediction API",
    version="1.0"
)

# Load trained model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)


class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def root():
    return {
        "message": "Iris ML Prediction API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(data: PredictionInput):

    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = int(model.predict(features)[0])

    classes = [
        "setosa",
        "versicolor",
        "virginica"
    ]

    return {
        "prediction": prediction,
        "class": classes[prediction]
    }
