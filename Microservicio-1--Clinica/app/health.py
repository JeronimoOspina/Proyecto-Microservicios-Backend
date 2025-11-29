from fastapi import APIRouter
from sqlalchemy import text
from app.database import engine

health_router = APIRouter()

@health_router.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception:
        return {"status": "error"}
