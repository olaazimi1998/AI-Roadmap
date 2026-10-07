# Dockerized ML API

A simple FastAPI machine learning API running inside Docker.

## Endpoints

### GET /

Returns API status.

### GET /health

Returns health status.

### POST /predict

Receives a value and returns a prediction.

Example:

```json
{
    "value": 80
}