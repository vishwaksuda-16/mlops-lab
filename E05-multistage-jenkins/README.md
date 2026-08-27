# E05 — Multi-Stage Jenkins Pipeline

## Aim

To implement a multi-stage CI/CD pipeline using Jenkins, Docker, Python, automated unit testing, static code analysis, and a simulated staging deployment.

---

## Objectives

- Create a Python application and automated tests.
- Create a declarative Jenkins pipeline.
- Execute the pipeline inside a Python 3.11 Docker container.
- Implement multiple stages in Jenkins.
- Install project dependencies automatically.
- Run unit tests using pytest.
- Perform static code analysis using Flake8.
- Simulate deployment to a staging environment.
- Integrate Jenkins with GitHub using a webhook.
- Automatically trigger the Jenkins pipeline whenever changes are pushed to the `main` branch.

---

## Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Git | Version control |
| GitHub | Remote repository |
| Jenkins | CI/CD automation |
| Docker | Pipeline execution environment |
| Python 3.11 | Application runtime inside Jenkins |
| Python 3.14 | Local development environment |
| pytest | Unit testing |
| Flake8 | Static code analysis |
| ngrok | Expose local Jenkins to GitHub webhook |
| WSL Ubuntu | Local development environment |

---

# 1. Project Structure

The experiment is stored inside the existing `mlops-lab` repository.

```text
E05-multistage-jenkins/
├── Jenkinsfile
├── app.py
├── test_app.py
├── requirements.txt
├── .gitignore
└── README.md
2. Python Application

The application contains a simple addition function.

app.py
def add(a, b):
    return a + b
3. Unit Tests

Two pytest test cases were created.

test_app.py
from app import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5

The tests verify the addition function using both positive and negative numbers.

4. Requirements
requirements.txt
pytest
flake8

The dependencies are installed automatically during the Jenkins pipeline.

5. Local Testing

A Python virtual environment was used for local testing to avoid modifying the system Python installation.

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Unit tests were executed using:

pytest -v

Static analysis was performed using:

flake8 app.py test_app.py

The unit tests completed successfully with:

2 passed
6. Jenkins Pipeline

A declarative Jenkinsfile was created with five stages.

Checkout
    ↓
Install Deps
    ↓
Unit Tests
    ↓
Static Analysis
    ↓
Deploy to Staging

The pipeline uses the Docker image:

python:3.11

This ensures that the Jenkins pipeline runs in a consistent Python environment.

7. Jenkinsfile
pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    options {
        skipDefaultCheckout(true)
    }

    environment {
        PYTHONPATH = "${WORKSPACE}/E05-multistage-jenkins/.python_packages"
        PATH = "${WORKSPACE}/E05-multistage-jenkins/.python_packages/bin:${PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Deps') {
            steps {
                dir('E05-multistage-jenkins') {
                    sh '''
                        python -m pip install \
                          --target="$WORKSPACE/E05-multistage-jenkins/.python_packages" \
                          -r requirements.txt
                    '''
                }
            }
        }

        stage('Unit Tests') {
            steps {
                dir('E05-multistage-jenkins') {
                    sh 'python -m pytest -v'
                }
            }
        }

        stage('Static Analysis') {
            steps {
                dir('E05-multistage-jenkins') {
                    sh 'python -m flake8 app.py test_app.py'
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                dir('E05-multistage-jenkins') {
                    sh 'echo "Deploying application to staging..."'
                    sh 'echo "Deployment successful!"'
                }
            }
        }
    }
}
8. Pipeline Stages
Stage 1 — Checkout

The Jenkins pipeline checks out the source code from the GitHub repository.

checkout scm

The E05 Jenkinsfile is located at:

E05-multistage-jenkins/Jenkinsfile
Stage 2 — Install Deps

Project dependencies are installed using:

python -m pip install -r requirements.txt

The packages are installed into a workspace-local directory to avoid Docker/Jenkins permission issues.

Stage 3 — Unit Tests

The automated tests are executed using:

python -m pytest -v

Expected result:

2 passed
Stage 4 — Static Analysis

Flake8 checks the Python source files:

python -m flake8 app.py test_app.py

A successful execution indicates that the source code passes the configured static analysis checks.

Stage 5 — Deploy to Staging

A simulated staging deployment is performed:

echo "Deploying application to staging..."
echo "Deployment successful!"

This experiment demonstrates the deployment stage without requiring an actual cloud or production server.

9. Jenkins Configuration

A Jenkins Pipeline job named:

E05-MultiStage-Jenkins

was created.

The pipeline uses:

Definition:
Pipeline script from SCM

SCM:
Git

Repository:
git@github.com:vishwaksuda-16/mlops-lab.git

Branch:
*/main

Script Path:
E05-multistage-jenkins/Jenkinsfile

The existing GitHub SSH credential was used for repository access.

10. Docker Integration

Jenkins was configured to use Docker for the pipeline agent.

The pipeline automatically pulls:

python:3.11

when the image is not already available.

The Docker container provides the Python environment in which the pipeline stages execute.

11. GitHub Webhook Integration

A GitHub webhook was configured to automatically notify Jenkins when changes are pushed to the repository.

Jenkins was configured with:

GitHub hook trigger for GITScm polling

The GitHub webhook uses the Jenkins webhook endpoint:

/github-webhook/

Because Jenkins is running locally, ngrok was used to expose the Jenkins server to GitHub.

The local Jenkins server runs at:

http://localhost:8080

The public ngrok URL was used as the base URL for the GitHub webhook.

The ngrok authentication token was not stored in the repository.

12. Automatic CI/CD Workflow

After configuring the webhook, pushing changes to the main branch triggers Jenkins automatically.

The workflow is:

Developer
    |
    | git push
    ↓
GitHub
    |
    | Webhook
    ↓
ngrok
    |
    ↓
Jenkins
    |
    ↓
Docker: python:3.11
    |
    ├── Checkout
    ├── Install Deps
    ├── Unit Tests
    ├── Static Analysis
    └── Deploy to Staging
13. Final Result

The multi-stage Jenkins pipeline executed successfully.

All five stages completed successfully:

Checkout              SUCCESS
Install Deps          SUCCESS
Unit Tests             SUCCESS
Static Analysis        SUCCESS
Deploy to Staging      SUCCESS

The unit test stage successfully executed:

2 passed

The staging deployment stage produced:

Deployment successful!

The GitHub webhook was also configured to automatically trigger the Jenkins pipeline following a push to main.
