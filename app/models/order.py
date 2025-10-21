from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Enum  # (Enum se usar status Enum)
from sqlalchemy.orm import relationship
from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"
  
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="PENDENTE")
    total = Column(Numeric(12, 2), nullable=False, default=0)  # <- era float
    items = relationship("OrderItem", back_populates="order")
    items_count = Column(Integer, default=0)

    def __init__(self, user_id: int, status: str = "PENDENTE", total: float = 0, items_count: int = 0):
        self.user_id = user_id
        self.status = status
        self.total = total
        self.items_count = items_count
