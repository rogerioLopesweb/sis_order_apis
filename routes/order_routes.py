from fastapi import APIRouter
order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def read_orders():
    return [{"order_id": 1, "item": "Item A"}, {"order_id": 2, "item": "Item B"}]