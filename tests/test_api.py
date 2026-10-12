from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import app

client = TestClient(app)

def test_health_check():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"

def test_get_guests():
    res = client.get("/guests")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_create_guest():
    res = client.post("/guests", json={
        "name": "Test Guest",
        "room": 999,
        "room_type": "single"
    })
    assert res.status_code == 200
    assert res.json()["name"] == "Test Guest"

def test_get_guest_not_found():
    res = client.get("/guests/99999")
    assert res.status_code == 404

def test_delete_guest():
    res = client.post("/guests", json={
        "name": "Delete Me",
        "room": 888,
        "room_type": "single"
    })
    guest_id = res.json()["id"]
    res = client.delete(f"/guests/{guest_id}")
    assert res.status_code == 200