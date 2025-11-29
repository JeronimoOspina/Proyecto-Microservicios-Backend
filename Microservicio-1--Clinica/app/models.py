from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date)
    gender = Column(String(20))
    status = Column(String(50), default="Activo")

    historias = relationship("HistoriaClinica", back_populates="paciente")

class TumorType(Base):
    __tablename__ = "tipos_tumor"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    system_affected = Column(String(150), nullable=False)

class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("pacientes.id"))
    tumor_type_id = Column(Integer, ForeignKey("tipos_tumor.id"))
    diagnosis_date = Column(Date)
    stage = Column(String(20))
    treatment_protocol = Column(Text)

    paciente = relationship("Paciente", back_populates="historias")
    tumor_type = relationship("TumorType")
