# app/routers/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from app.db.session import get_db
from app.models import User 

router = APIRouter(prefix="/auth", tags=["auth"])




# ====== Endpoints ======
@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = (
        db.query(User)
        .filter(User.email == email, User.password == password)
        .first()
    )
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.id}


@router.post("/create-account")
def create_account(email: str, name: str, password: str, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.email == email).first()
    if exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")

    new_user = User(name=name, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Account created successfully", "user_id": new_user.id}


@router.post("/reset-password")
def reset_password(email: str, new_password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user.password = new_password
    db.commit()
    return {"message": "Password reset successful"}
