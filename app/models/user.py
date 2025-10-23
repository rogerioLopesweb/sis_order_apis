from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric, Enum  # (Enum se usar status Enum)
from sqlalchemy.orm import relationship
from app.db.base import Base


# classe que representa a tabela users no banco de dados
class User(Base):
    __tablename__ = "users"

    id    = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name  = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    active = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)
    
    # Construtor da classe
    def __init__(self, name: str, email: str, password: str, active: bool = True, admin: bool = False):
        
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
