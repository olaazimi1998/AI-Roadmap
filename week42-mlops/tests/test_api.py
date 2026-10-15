from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_predict():
    response = client.post(
        "/predict",
        json={
            "tenure_months": 12,
            "monthly_charges": 75.5,
            "support_calls": 2,
        },
    )

    assert response.status_code == 200
    assert response.json()["prediction"] == "unknown"


def test_predict_rejects_negative_values():
    response = client.post(
        "/predict",
        json={
            "tenure_months": -1,
            "monthly_charges": 75.5,
            "support_calls": 2,
        },
    )

    assert response.status_code == 422