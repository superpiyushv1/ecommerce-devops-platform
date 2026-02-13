from app.app import app
from unittest.mock import MagicMock

def test_home_route(monkeypatch):
    # Mock Redis
    mock_redis = MagicMock()
    mock_redis.incr.return_value = 1

    # Patch get_redis() used inside app.app
    monkeypatch.setattr("app.app.get_redis", lambda: mock_redis)

    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Ecommerce DevOps Platform" in response.data

