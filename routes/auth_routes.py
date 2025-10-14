from fastapi import APIRouter
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
async def login(credentials: dict):
    return {"message": "Login successful", "credentials": credentials}
