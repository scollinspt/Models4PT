from fastapi.testclient import TestClient

from models4pt.app import app

client = TestClient(app)


def test_root_returns_message() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Models4PT backend is running."}


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
