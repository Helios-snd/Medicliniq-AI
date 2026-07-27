import uuid

from sqlalchemy.orm import Session

from app.models.vital import Vital


def create_vital(
    db: Session,
    *,
    vital: Vital,
) -> Vital:
    db.add(vital)
    db.commit()
    db.refresh(vital)

    return vital


def get_vitals_by_user_id(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> list[Vital]:
    return (
        db.query(Vital)
        .filter(Vital.user_id == user_id)
        .all()
    )


def get_vital_by_id(
    db: Session,
    *,
    vital_id: uuid.UUID,
) -> Vital | None:
    return (
        db.query(Vital)
        .filter(Vital.id == vital_id)
        .first()
    )


def update_vital(
    db: Session,
    *,
    vital: Vital,
) -> Vital:
    db.commit()
    db.refresh(vital)

    return vital


def delete_vital(
    db: Session,
    *,
    vital: Vital,
) -> None:
    db.delete(vital)
    db.commit()