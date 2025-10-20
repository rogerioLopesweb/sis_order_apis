from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Enum  # (Enum se usar status Enum)
from sqlalchemy.orm import relationship
from db.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"



    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
    price = Column(Numeric(12, 2), nullable=False, default=0)  # <- era float
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
    total = Column(Numeric(12, 2), nullable=False, default=0)  # <- era float
    
    def __init__(self, order_id: int, product_id: int, quantity: int = 1, price: float = 0, total: float = 0):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.total = total