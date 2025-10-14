# install dependencies 
# pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart
# command to run the app
# uvicorn main:app --reload
# pip freeze > requirements.txt para gerar o requirements.txt

#Inicializa o FastAPI
from fastapi import FastAPI, Depends, HTTPException, status
app = FastAPI()

# importa as rotas
from routes.auth_routes import auth_router
from routes.order_routes import order_router
  
# inclui as rotas na aplicação
app.include_router(auth_router)
app.include_router(order_router)