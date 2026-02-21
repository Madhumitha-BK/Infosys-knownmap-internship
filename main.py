from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models
from auth import hash_password, verify_password, create_access_token
from dataset import router as dataset_router

app = FastAPI()
app.include_router(dataset_router)

Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "KnowMap API with Authentication 🚀"}


# =========================
# REGISTER
# =========================
@app.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    hashed_pw = hash_password(password)

    new_user = models.User(
        username=username,
        email=email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully ✅"}


# =========================
# LOGIN WITH JWT
# =========================
@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid password")

    access_token = create_access_token({"sub": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


