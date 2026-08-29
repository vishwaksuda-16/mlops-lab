## E08 README — Outline

```text
# E08 - DVC Pipeline

## Objective
Set up a DVC-based ML pipeline and demonstrate data/model metric versioning.

## Tools
- Python
- DVC
- Git
- Scikit-learn

## Project Structure
data.csv
prepare.py
train.py
evaluate.py
dvc.yaml
dvc.lock
metrics.json

## Steps

### 1. Create Python Environment
Commands used to create and activate .venv and install DVC/dependencies.

### 2. Initialize DVC
dvc init --subdir

### 3. Track Dataset
dvc add data.csv

### 4. Create DVC Pipeline
Pipeline stages:
data.csv → prepare → train → evaluate

### 5. Run Pipeline
dvc repro

### 6. View Pipeline
dvc dag

### 7. View Metrics
dvc metrics show

### 8. Create Version 1
Git commit + tag:
e08-v1

Accuracy: 1.00

### 9. Modify Dataset/Model
Modified the experiment and reran:
dvc repro

### 10. Create Final Version
Git commit + tag:
e08-final

Accuracy: 0.85

### 11. Compare Metrics
dvc metrics diff e08-v1

Shows:
1.00 → 0.85

## Result
Successfully demonstrated:
- DVC data tracking
- Reproducible ML pipeline
- Metric tracking
- Version comparison
```

### Steps to finish E08

You only need to do these now:

**1. Create/update README**

```bash
nano README.md
```

Paste the outline above.

**2. Save it**

`Ctrl + O` → Enter → `Ctrl + X`

**3. Commit**

```bash
git add README.md
git commit -m "E08: add DVC pipeline documentation"
```

**4. Push**

```bash
git push origin main
```

**5. Final verification**

```bash
dvc status
dvc dag
dvc metrics show
dvc metrics diff e08-v1
git status
```
