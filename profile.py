from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import UserProfile  # your UserProfile model from profile schema

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

def get_profile(db: Session, user_id: int):
    return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

@app.post("/profile/interests")
def save_interests(user_id: int, interests: list):
    db = SessionLocal()
    profile = get_profile(db, user_id)
    if not profile:
        profile = UserProfile(user_id=user_id, interests=",".join(interests))
        db.add(profile)
    else:
        profile.interests = ",".join(interests)
    db.commit()
    db.close()
    return {"message": "Interests saved"}

@app.get("/profile/interests/{user_id}")
def get_interests(user_id: int):
    db = SessionLocal()
    profile = get_profile(db, user_id)
    db.close()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")