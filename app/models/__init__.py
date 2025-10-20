# models/__init__.py
from app.db.base import Base  # expõe o Base

# importe as models para registrá-las no metadata
from .user import User      # noqa
from .product import Product # noqa
from .order import Order     # noqa
from .orderItem import OrderItem  # noqa
