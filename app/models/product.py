from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, Enum  # (Enum se usar status Enum)
from sqlalchemy.orm import relationship
from app.db.base import Base


# classe que representa a tabela products no banco de dados
class Product(Base):
    __tablename__ = "products"

    id    = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name  = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric(12, 2), nullable=False, default=0)  # <- era float
    in_stock = Column(Boolean, default=True)
    
    # Construtor da classe
    def __init__(self, name: str, description: str, price: float, in_stock: bool = True):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock