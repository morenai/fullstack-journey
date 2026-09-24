from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, GuestDB, create_tables

app = FastAPI()
create_tables()

class Guest(BaseModel):
    name: str
    room: int
    room_type: str
    checked_in: bool = False

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Hotel API is running!"}

@app.get("/guests")
def get_guests(db: Session = Depends(get_db)):
    return db.query(GuestDB).all()

@app.post("/guests")
def create_guest(guest: Guest, db: Session = Depends(get_db)):
    db_guest = GuestDB(**guest.model_dump())
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return db_guest