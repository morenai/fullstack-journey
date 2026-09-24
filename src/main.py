from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/guests/{guest_id}")
def get_guest(guest_id: int, db: Session = Depends(get_db)):
    guest = db.query(GuestDB).filter(GuestDB.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest

@app.delete("/guests/{guest_id}")
def delete_guest(guest_id: int, db: Session = Depends(get_db)):
    guest = db.query(GuestDB).filter(GuestDB.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    db.delete(guest)
    db.commit()
    return {"message": f"Guest {guest_id} deleted"}