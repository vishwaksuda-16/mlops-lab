# E09 - MLflow Model Registry Lifecycle

## Objective

Register the best model from E07 using the MLflow Model Registry, validate it, promote it to Production, and use the Production model for batch inference.

## Tools

- Python 3.11
- MLflow
- Scikit-learn
- MLflow Client API

## Steps

### 1. Start MLflow Server

```bash
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts

Open:

http://127.0.0.1:5000
2. Select Best Model

Selected the Logistic Regression model from E07.

Run ID:

99d3fa7845e04803bbe65166de1e1399
3. Register Model

Registered the model using the MLflow Python API.

Model name:

WineQualityModel

Version:

Version 1
4. Add Metadata

Added model description and tag:

dataset = wine-quality-v1
5. Assign Staging Alias

Assigned:

staging

to Version 1.

6. Validate Model

Loaded the Staging model and checked its accuracy against the validation threshold.

Accuracy: 0.9649
Validation: PASSED
7. Promote to Production

After successful validation, assigned the:

champion

alias to Version 1.

8. Batch Inference

Loaded the Production/Champion model and generated predictions on the test dataset.

Output:

predictions.csv
Result

Successfully demonstrated the MLflow Model Registry lifecycle:

E07 Best Model
      ↓
Registered
      ↓
Staging
      ↓
Validation
      ↓
Champion / Production
      ↓
Batch Inference
