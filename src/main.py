from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, GuestDB, ReservationDB, UserDB, create_tables
from auth import hash_password, verify_password, create_token, verify_token

app = FastAPI()
create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models ---
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

class UserRegister(BaseModel):
    email: str
    password: str

# --- DB Session ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Auth ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(UserDB).filter(UserDB.email == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# --- Endpoints ---
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
def delete_guest(guest_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
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

@app.post("/auth/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing = db.query(UserDB).filter(UserDB.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = UserDB(email=user.email, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    return {"message": "User created successfully"}

@app.post("/auth/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.email == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}