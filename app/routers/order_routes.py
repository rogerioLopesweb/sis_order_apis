from fastapi import APIRouter
router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/")
async def read_orders():
    return [{"order_id": 1, "item": "Item A"}, {"order_id": 2, "item": "Item B"}]