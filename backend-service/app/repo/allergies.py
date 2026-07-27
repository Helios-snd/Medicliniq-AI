import uuid

from sqlalchemy.orm import Session

from app.models.allergies import Allergy


def get_allergies_by_user_id(
    db: Session,
    *,
    user_id: uuid.UUID,
):
    return (
        db.query(Allergy)
        .filter(Allergy.user_id == user_id)
        .all()
    )


def get_allergy_by_id(
    db: Session,
    *,
    allergy_id: uuid.UUID,
):
    return (
        db.query(Allergy)
        .filter(Allergy.id == allergy_id)
        .first()
    )


def create_allergy(
    db: Session,
    *,
    allergy: Allergy,
):
    db.add(allergy)
    db.commit()
    db.refresh(allergy)
    return allergy


def update_allergy(
    db: Session,
    *,
    allergy: Allergy,
):
    db.commit()
    db.refresh(allergy)
    return allergy


def delete_allergy(
    db: Session,
    *,
    allergy: Allergy,
):
    db.delete(allergy)
    db.commit()

    