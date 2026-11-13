import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_get_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.parametrize("query, expected_status", [
    ("python", 200),
    ("fastapi", 200),
    ("", 400),
])
def test_search(query, expected_status):
    response = client.get(f"/search?q={query}")
    assert response.status_code == expected_status

def test_item_not_found():
    response = client.get("/items/999999")
    assert response.status_code == 404

def test_invalid_payload():
    response = client.post("/items/", json={})
    assert response.status_code == 422