from sqlalchemy.orm import Session
from app.models import Paciente, TumorType, HistoriaClinica

class PacienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, paciente: Paciente):
        self.db.add(paciente)
        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def get(self, id: int):
        return self.db.query(Paciente).filter(Paciente.id == id).first()

    def update(self, paciente: Paciente):
        self.db.commit()
        self.db.refresh(paciente)
        return paciente


class TumorRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, tumor: TumorType):
        self.db.add(tumor)
        self.db.commit()
        self.db.refresh(tumor)
        return tumor

    def list(self):
        return self.db.query(TumorType).all()


class HistoriaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, historia: HistoriaClinica):
        self.db.add(historia)
        self.db.commit()
        self.db.refresh(historia)
        return historia

    def by_patient(self, patient_id: int):
        return self.db.query(HistoriaClinica).filter(HistoriaClinica.patient_id == patient_id).all()
