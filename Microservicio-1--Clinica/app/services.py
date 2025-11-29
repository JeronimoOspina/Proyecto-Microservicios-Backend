from app.repositories import *
from app.mappers import *

class PacienteService:
    def __init__(self, db): self.repo = PacienteRepository(db)

    def crear(self, dto):
        model = paciente_from_create(dto)
        return paciente_to_response(self.repo.create(model))

    def obtener(self, id):
        model = self.repo.get(id)
        if not model: raise Exception("Paciente no encontrado")
        return paciente_to_response(model)

    def actualizar(self, id, dto):
        model = self.repo.get(id)
        for k, v in dto.dict(exclude_unset=True).items():
            setattr(model, k, v)
        return paciente_to_response(self.repo.update(model))


class TumorService:
    def __init__(self, db): self.repo = TumorRepository(db)

    def crear(self, dto):
        return tumor_to_response(self.repo.create(tumor_from_create(dto)))

    def listar(self):
        return [tumor_to_response(t) for t in self.repo.list()]


class HistoriaService:
    def __init__(self, db): self.repo = HistoriaRepository(db)

    def crear(self, dto):
        return historia_to_response(self.repo.create(historia_from_create(dto)))

    def por_paciente(self, patient_id):
        return [historia_to_response(h) for h in self.repo.by_patient(patient_id)]
