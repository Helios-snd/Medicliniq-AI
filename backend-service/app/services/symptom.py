import uuid

from fastapi import (
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.models.symptom import Symptom

from app.schemas.symptom import (
    SymptomCreate,
    SymptomUpdate,
)

from app.repo.symptom import (
    create_symptom,
    get_symptoms_by_user_id,
    get_symptom_by_id,
    update_symptom,
    delete_symptom,
)


def create_symptom_service(
    db: Session,
    *,
    user_id: uuid.UUID,
    payload: SymptomCreate,
) -> Symptom:

    symptom = Symptom(
        user_id=user_id,
        symptom_name=payload.symptom_name,
        severity=payload.severity,
        duration=payload.duration,
        notes=payload.notes,
    )

    return create_symptom(
        db,
        symptom=symptom,
    )


def get_symptoms_service(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> list[Symptom]:

    return get_symptoms_by_user_id(
        db,
        user_id=user_id,
    )


def get_symptom_service(
    db: Session,
    *,
    symptom_id: uuid.UUID,
    user_id: uuid.UUID,
) -> Symptom:

    symptom = get_symptom_by_id(
        db,
        symptom_id=symptom_id,
    )

    if not symptom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Symptom not found",
        )

    if symptom.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    return symptom


def update_symptom_service(
    db: Session,
    *,
    symptom_id: uuid.UUID,
    user_id: uuid.UUID,
    payload: SymptomUpdate,
) -> Symptom:

    symptom = get_symptom_by_id(
        db,
        symptom_id=symptom_id,
    )

    if not symptom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Symptom not found",
        )

    if symptom.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    if payload.severity is not None:
        symptom.severity = payload.severity

    if payload.duration is not None:
        symptom.duration = payload.duration

    if payload.notes is not None:
        symptom.notes = payload.notes

    return update_symptom(
        db,
        symptom=symptom,
    )


def delete_symptom_service(
    db: Session,
    *,
    symptom_id: uuid.UUID,
    user_id: uuid.UUID,
) -> None:

    symptom = get_symptom_by_id(
        db,
        symptom_id=symptom_id,
    )

    if not symptom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Symptom not found",
        )

    if symptom.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    delete_symptom(
        db,
        symptom=symptom,
    )

    