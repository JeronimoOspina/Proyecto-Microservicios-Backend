from fastapi import FastAPI
from app.routers import router
from app.health import health_router
from app.database import Base, engine

app = FastAPI(
    title="Microservicio 1 - Clínica",
    description="Servicios clínicos: gestión de pacientes, tumores e historias clínicas.",
    version="1.0.0"
)

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

# Rutas
app.include_router(health_router, tags=["Health"])
app.include_router(router, prefix="/api/v1", tags=["Clínica"])
