# E07 - MLflow Multi-Model Experiment Tracking

## Objective

Train multiple machine learning classification models and use MLflow to track, compare, and visualize their experiments, metrics, parameters, and artifacts.

## Tools Used

- Python 3.11
- MLflow
- scikit-learn
- XGBoost
- Pandas
- Matplotlib
- SQLite

## Models

Three classification models were trained:

1. Logistic Regression
2. Random Forest
3. XGBoost

## Dataset

The scikit-learn Breast Cancer Wisconsin dataset was used.

The dataset was divided into:

- 80% training data
- 20% testing data

A fixed random state of 42 was used for reproducibility.

## Project Structure

```text
E07-mlflow-experiment/
├── calculator.py
├── train_models.py
├── requirements.txt
├── .gitignore
└── README.md

MLflow tracking data and generated artifacts are intentionally excluded from Git using .gitignore.

Setup

Create and activate a Python 3.11 virtual environment:

uv venv --python 3.11
source .venv/bin/activate

Install dependencies:

uv pip install -r requirements.txt
Start MLflow Server

Start the MLflow tracking server:

mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./artifacts

The MLflow UI is available at:

http://127.0.0.1:5000
Run the Experiment

In a second terminal, activate the virtual environment:

source .venv/bin/activate

Run:

python train_models.py

The script trains and logs all three models to the MLflow experiment:

E07-Multi-Model-Experiment
Metrics Tracked

For every model, the following metrics were logged:

Accuracy
Precision
Recall
F1 Score

The model itself was also logged as an MLflow artifact.

A confusion matrix image was generated and logged for each run.

Experimental Results
Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	0.9649	0.9595	0.9861	0.9726
Random Forest	0.9561	0.9589	0.9722	0.9655
XGBoost	0.9474	0.9459	0.9722	0.9589
Model Comparison

Logistic Regression achieved the best overall performance in this experiment.

It obtained:

Highest accuracy: 96.49%
Highest recall: 98.61%
Highest F1 score: 97.26%

Random Forest achieved the highest precision among the three models.

MLflow Tracking

MLflow was used to provide centralized tracking for all model runs.

Each run contains:

Model name
Model parameters
Evaluation metrics
Trained model
Confusion matrix artifact

The MLflow comparison interface was used to compare the three runs.

Result

The experiment successfully demonstrated multi-model experiment tracking using MLflow.

Three different machine learning models were trained under the same experimental setup, and their performance was recorded and compared using MLflow.
