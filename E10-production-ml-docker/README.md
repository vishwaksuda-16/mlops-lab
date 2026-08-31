# E10 - Production ML Docker Image

## Objective

Containerize a machine learning prediction API and deploy the Docker image to Docker Hub.

## Tools

- Python 3.11
- FastAPI
- Scikit-learn
- Docker
- Docker Hub

## Steps

### 1. Train Model

Trained a Random Forest classifier using the Iris dataset.

Model saved as:

```text
model/model.pkl
2. Create API

Created a FastAPI application with:

GET  /health
POST /predict
3. Test API

Verified the API locally using curl.

4. Build Docker Image
docker build -t iris-ml-api:1.0 .
5. Run Container
docker run -d --name iris-ml-api -p 8000:8000 iris-ml-api:1.0
6. Health Check
curl http://127.0.0.1:8000/health

Result:

{"status":"healthy"}
7. Prediction

Tested /predict endpoint successfully and received the predicted Iris class.

8. Docker Hub

Tagged and pushed the image to Docker Hub:

YOUR_USERNAME/iris-ml-api:1.0
Result

Successfully created and tested a production-ready Dockerized ML prediction API and published the image to Docker Hub.
