content = """from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./hotel.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class GuestDB(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    room = Column(Integer)
    room_type = Column(String)
    checked_in = Column(Boolean, default=False)

def create_tables():
    Base.metadata.create_all(bind=engine)
"""
with open("database.py", "w") as f:
    f.write(content)