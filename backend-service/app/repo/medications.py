import uuid

from sqlalchemy.orm import Session

from app.models.medications import Medication


def get_medications_by_user_id(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> list[Medication]:
    return (
        db.query(Medication)
        .filter(Medication.user_id == user_id)
        .all()
    )


def get_medication_by_id(
    db: Session,
    *,
    medication_id: uuid.UUID,
) -> Medication | None:
    return (
        db.query(Medication)
        .filter(Medication.id == medication_id)
        .first()
    )


def create_medication(
    db: Session,
    *,
    medication: Medication,
) -> Medication:
    db.add(medication)
    db.commit()
    db.refresh(medication)
    return medication


def update_medication(
    db: Session,
    *,
    medication: Medication,
) -> Medication:
    db.commit()
    db.refresh(medication)
    return medication


def delete_medication(
    db: Session,
    *,
    medication: Medication,
) -> None:
    db.delete(medication)
    db.commit()

    