from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, GuestDB, ReservationDB, create_tables

app = FastAPI()
create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Guest(BaseModel):
    name: str
    room: int
    room_type: str
    checked_in: bool = False

class Reservation(BaseModel):
    guest_id: int
    check_in: str
    check_out: str
    room: int

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

@app.get("/guests/{guest_id}")
def get_guest(guest_id: int, db: Session = Depends(get_db)):
    guest = db.query(GuestDB).filter(GuestDB.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest

@app.post("/guests")
def create_guest(guest: Guest, db: Session = Depends(get_db)):
    db_guest = GuestDB(**guest.model_dump())
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return db_guest

@app.delete("/guests/{guest_id}")
def delete_guest(guest_id: int, db: Session = Depends(get_db)):
    guest = db.query(GuestDB).filter(GuestDB.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    db.delete(guest)
    db.commit()
    return {"message": f"Guest {guest_id} deleted"}

@app.get("/reservations")
def get_reservations(db: Session = Depends(get_db)):
    return db.query(ReservationDB).all()

@app.post("/reservations")
def create_reservation(reservation: Reservation, db: Session = Depends(get_db)):
    db_res = ReservationDB(**reservation.model_dump())
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    return db_res

@app.get("/guests/{guest_id}/reservations")
def get_guest_reservations(guest_id: int, db: Session = Depends(get_db)):
    guest = db.query(GuestDB).filter(GuestDB.id == guest_id).first()
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    reservations = db.query(ReservationDB).filter(ReservationDB.guest_id == guest_id).all()
    return {"guest": guest, "reservations": reservations}