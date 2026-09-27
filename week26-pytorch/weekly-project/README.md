# PyTorch Prediction API

This project trains a small PyTorch linear regression model and exposes it through a FastAPI endpoint. The model learns the relationship `y = 2x` from the sample data in `train.py`.

## Requirements

- Python 3.10+
- PyTorch
- FastAPI
- Uvicorn

Install the dependencies:

```powershell
python -m pip install torch fastapi uvicorn
```

## Run the project

Open PowerShell in this folder:

```powershell
python train.py
python -m uvicorn api:app --reload
```

Training creates `model.pth` next to the Python files. The API loads that checkpoint using an absolute path based on `api.py`, so it can also be started from another working directory.

## Endpoints

### Health check

```text
GET /
```

Example response:

```json
{"message":"PyTorch Model API is running"}
```

### Prediction

```text
GET /predict?x=6
```

Example response:

```json
{"input":6.0,"prediction":12.0}
```

Open the interactive API documentation at `http://127.0.0.1:8000/docs` after starting Uvicorn.

## Test from PowerShell

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/"
Invoke-RestMethod "http://127.0.0.1:8000/predict?x=6"
```
