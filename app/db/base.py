from sqlalchemy.orm import declarative_base
Base = declarative_base()
# define the base class for declarative class definitions

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass