from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import *
from app.services import *

router = APIRouter()

@router.post("/pacientes/", response_model=PacienteResponseDTO)
def crear_paciente(dto: PacienteCreateDTO, db: Session = Depends(get_db)):
    return PacienteService(db).crear(dto)

@router.get("/pacientes/{id}", response_model=PacienteResponseDTO)
def obtener_paciente(id: int, db: Session = Depends(get_db)):
    return PacienteService(db).obtener(id)

@router.put("/pacientes/{id}", response_model=PacienteResponseDTO)
def actualizar_paciente(id: int, dto: PacienteUpdateDTO, db: Session = Depends(get_db)):
    return PacienteService(db).actualizar(id, dto)


@router.post("/tumores/", response_model=TumorTypeResponseDTO)
def crear_tumor(dto: TumorTypeCreateDTO, db: Session = Depends(get_db)):
    return TumorService(db).crear(dto)

@router.get("/tumores/", response_model=list[TumorTypeResponseDTO])
def listar_tumores(db: Session = Depends(get_db)):
    return TumorService(db).listar()


@router.post("/historias/", response_model=HistoriaResponseDTO)
def crear_historia(dto: HistoriaCreateDTO, db: Session = Depends(get_db)):
    return HistoriaService(db).crear(dto)

@router.get("/historias/paciente/{id}", response_model=list[HistoriaResponseDTO])
def historias_por_paciente(id: int, db: Session = Depends(get_db)):
    return HistoriaService(db).por_paciente(id)
