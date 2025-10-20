from fastapi import APIRouter
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(credentials: dict):
    return {"message": "Login successful", "credentials": credentials}
