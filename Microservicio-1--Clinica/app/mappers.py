from app.models import Paciente, TumorType, HistoriaClinica
from app.schemas import *

def paciente_from_create(dto: PacienteCreateDTO):
    return Paciente(**dto.dict())

def paciente_to_response(model: Paciente):
    return PacienteResponseDTO.from_orm(model)

def tumor_from_create(dto: TumorTypeCreateDTO):
    return TumorType(**dto.dict())

def tumor_to_response(model: TumorType):
    return TumorTypeResponseDTO.from_orm(model)

def historia_from_create(dto: HistoriaCreateDTO):
    return HistoriaClinica(**dto.dict())

def historia_to_response(model: HistoriaClinica):
    return HistoriaResponseDTO.from_orm(model)
