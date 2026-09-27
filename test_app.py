import os

os.environ.setdefault("APP_CONFIG_KEY", "test-value")

from app import app  # noqa: E402


def test_index():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "running"
