# E06 - GitHub Actions with Test Coverage Gate

## Objective

Implement a GitHub Actions CI pipeline that automatically runs Python unit tests and enforces a minimum test coverage requirement before changes can be merged into the main branch.

## Tools Used

- Python 3.11
- pytest
- pytest-cov
- GitHub Actions
- GitHub Pull Requests
- Git

## Project Structure

```text
E06-github-actions-coverage/
├── calculator.py
├── test_calculator.py
├── .gitignore
└── README.md

.github/
└── workflows/
    └── ci.yml

The GitHub Actions workflow is stored at the repository root because GitHub Actions detects workflow files from:

.github/workflows/

Calculator Application

calculator.py contains basic arithmetic functions:

Addition
Subtraction
Multiplication
Division
Unit Testing

Tests were written using pytest.

Run the tests locally:

pytest -v

Expected result:

4 passed
Test Coverage

Coverage was measured using pytest-cov:

pytest --cov=calculator --cov-report=term-missing

The tests achieved approximately 90% coverage.

GitHub Actions Workflow

The workflow is defined in:

.github/workflows/ci.yml

The workflow is triggered whenever a Pull Request targets the main branch.

Pipeline Stages
Checkout repository
Set up Python 3.11
Install pytest and pytest-cov
Run unit tests
Calculate test coverage
Enforce an 80% minimum coverage requirement

The coverage gate is implemented using:

pytest --cov=calculator --cov-report=term-missing --cov-fail-under=80
Coverage Gate Demonstration

The pipeline was first executed with the complete test suite and passed successfully.

Coverage was then intentionally reduced below 80% by removing test cases.

The GitHub Actions workflow correctly failed because the required 80% coverage threshold was not reached.

The test cases were then restored and pushed again.

The workflow successfully passed after coverage returned above the required threshold.

Pull Request Validation

An E06-coverage-test branch was created and a Pull Request was opened against main.

The Pull Request demonstrated:

Successful GitHub Actions execution
Coverage enforcement
Intentional coverage failure
Successful recovery after restoring tests
Result

The experiment successfully demonstrates Continuous Integration with automated testing and a test-coverage quality gate.

Changes that reduce test coverage below 80% are prevented from passing the CI check.
