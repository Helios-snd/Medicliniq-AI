import uuid
from sqlalchemy.orm import Session
from app.models.medical_history import MedicalHistory


def get_medical_history_by_user_id(db: Session, *, user_id: uuid.UUID) -> MedicalHistory | None:
    return(
        db.query(MedicalHistory).filter(MedicalHistory.user_id == user_id).first()
    )


def create_medical_history(db: Session, *, medical_history: MedicalHistory)-> MedicalHistory:
    db.add(medical_history)
    db.commit()
    db.refresh(medical_history)
    return medical_history


def update_medical_history(db: Session, *, medical_history: MedicalHistory)-> MedicalHistory:
    db.commit()
    db.refresh(medical_history)
    return medical_history

