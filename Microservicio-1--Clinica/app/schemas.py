from pydantic import BaseModel
from datetime import date
from typing import Optional


class PacienteCreateDTO(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    gender: str


class PacienteUpdateDTO(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    status: Optional[str] = None



class PacienteResponseDTO(PacienteCreateDTO):
    id: int
    status: str

    class Config:
        from_attributes = True



class TumorTypeCreateDTO(BaseModel):
    name: str
    system_affected: str


class TumorTypeResponseDTO(TumorTypeCreateDTO):
    id: int

    class Config:
        from_attributes = True


class HistoriaCreateDTO(BaseModel):
    patient_id: int
    tumor_type_id: int
    diagnosis_date: date
    stage: str
    treatment_protocol: str


class HistoriaResponseDTO(HistoriaCreateDTO):
    id: int

    class Config:
        from_attributes = True
