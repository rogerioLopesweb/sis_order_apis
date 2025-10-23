# app/routers/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models import User
from app.security import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

# Constantes
MAX_PASSWORD_BYTES = 72  # Limite do bcrypt

# ====== Endpoints ======
@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.id}


@router.post("/create-account")
def create_account(email: str, name: str, password: str, db: Session = Depends(get_db)):
    # Verificar se a conta já existe primeiro
    exists = db.query(User).filter(User.email == email).first()
    if exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")

    try:
        # Criar o hash da senha usando bcrypt diretamente
        password_hashed = hash_password(password)
        
        # Criar e salvar o usuário
        new_user = User(name=name, email=email, password=password_hashed)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "Account created successfully", "user_id": new_user.id}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating account: {str(e)}"
        )


@router.post("/reset-password")
def reset_password(email: str, new_password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    try:
        # Atualizar a senha com novo hash usando bcrypt diretamente
        user.password = hash_password(new_password)
        db.commit()
        return {"message": "Password reset successful"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error resetting password: {str(e)}"
        )
