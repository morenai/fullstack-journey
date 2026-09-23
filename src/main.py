# Day 07 — FastAPI POST requests & Pydantic

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Guest(BaseModel):
    name: str
    room: int
    room_type: str
    checked_in: bool = False

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Hotel API is running!"}

@app.get("/rooms")
def get_rooms():
    return [
        {"number": 101, "type": "single", "occupied": False},
        {"number": 102, "type": "double", "occupied": True},
        {"number": 103, "type": "suite", "occupied": False}
    ]

@app.get("/rooms/{room_id}")
def get_room(room_id: int):
    return {"number": room_id, "type": "single", "occupied": False}

@app.post("/guests")
def create_guest(guest: Guest):
    return {"message": "Guest created", "guest": guest}