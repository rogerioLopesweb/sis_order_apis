# app/db/session.py
from __future__ import annotations
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Sobe de .../app/db/session.py -> .../app -> .../sis_order_apis (raiz)
BASE_DIR = Path(__file__).resolve().parents[2]

# garante que a pasta db exista
DB_DIR = BASE_DIR / "db"
DB_DIR.mkdir(parents=True, exist_ok=True)

# Usa DATABASE_URL se existir; senão monta absoluto para o SQLite
env_url = os.getenv("DATABASE_URL")
if env_url and env_url.startswith("sqlite:///") and not env_url.startswith("sqlite:////"):
    # se vier relativo em env, normaliza para absoluto
    rel_path = env_url.replace("sqlite:///", "")
    abs_path = (BASE_DIR / rel_path).resolve()
    DATABASE_URL = f"sqlite:///{abs_path.as_posix()}"
elif env_url:
    DATABASE_URL = env_url
else:
    DATABASE_URL = f"sqlite:///{(DB_DIR / 'database_dev.db').as_posix()}"

# Para FastAPI + SQLite (threads)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite:///") else {},
    future=True,
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
# Dependência para obter sessão do banco de dados
def get_db():
    try:
        db = SessionLocal() 
        yield db
    finally:
        db.close()
