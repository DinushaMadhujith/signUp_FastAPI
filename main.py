from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocate
import models
from typing import Annotated

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Signup model for API
class SignupBase(BaseModel):
    name: str
    email: str
    phone_number: str
    type: str  # customer, labor, admin, deliver, farmer
    password: str

def get_db():
    db = SessionLocate()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/signup/")
async def create_signup(signup: SignupBase, db: db_dependency):
    # Check if email already exists
    existing_user = db.query(models.Signup).filter(models.Signup.email == signup.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Add new user
    db_signup = models.Signup(
        name=signup.name,
        email=signup.email,
        phone_number=signup.phone_number,
        type=signup.type,
        password=signup.password  # Ideally, use a hashed password
    )
    db.add(db_signup)
    db.commit()
    db.refresh(db_signup)
    return {"message": "Signup successful", "user_id": db_signup.id}
