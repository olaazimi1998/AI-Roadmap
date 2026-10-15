from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_predict():
    response = client.post(
        "/predict",
        json={
            "tenure": 6,
            "monthly_charges": 100,
            "support_calls": 5,
        },
    )

    assert response.status_code == 200

    result = response.json()

    assert result["prediction"] in [0, 1]
    assert 0 <= result["risk_score"] <= 1
    assert result["risk_label"] in ["High", "Low"]


def test_negative_tenure_is_rejected():
    response = client.post(
        "/predict",
        json={
            "tenure": -1,
            "monthly_charges": 100,
            "support_calls": 5,
        },
    )

    assert response.status_code == 422