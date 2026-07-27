import uuid

from sqlalchemy.orm import Session

from app.models.symptom import Symptom


def create_symptom(
    db: Session,
    *,
    symptom: Symptom,
) -> Symptom:
    db.add(symptom)
    db.commit()
    db.refresh(symptom)

    return symptom


def get_symptoms_by_user_id(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> list[Symptom]:
    return (
        db.query(Symptom)
        .filter(Symptom.user_id == user_id)
        .all()
    )


def get_symptom_by_id(
    db: Session,
    *,
    symptom_id: uuid.UUID,
) -> Symptom | None:
    return (
        db.query(Symptom)
        .filter(Symptom.id == symptom_id)
        .first()
    )


def update_symptom(
    db: Session,
    *,
    symptom: Symptom,
) -> Symptom:
    db.commit()
    db.refresh(symptom)

    return symptom


def delete_symptom(
    db: Session,
    *,
    symptom: Symptom,
) -> None:
    db.delete(symptom)
    db.commit()