# install dependencies 
# pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart
# command to run the app
# uvicorn main:app --reload
# pip freeze > requirements.txt para gerar o requirements.txt
# pip install sqlalchemy_utils
# pip install alembic

#py -3.11 -m alembic revision --autogenerate -m "initial schema"
#py -3.11 -m alembic upgrade head

#Inicializa o FastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from app.db.session import engine
from app.db.base import Base
from app.routers.auth_routes import router as auth_router
from app.routers.order_routes import router as order_router
app = FastAPI()
Base.metadata.create_all(bind=engine)

  
# inclui as rotas na aplicação
app.include_router(auth_router)
app.include_router(order_router)