import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.medical_history import MedicalHistory
from app.repo.medical_history import (
    get_medical_history_by_user_id,
    create_medical_history,
    update_medical_history,
)
from app.schemas.medical_history import (
    MedicalHistoryCreate,
    MedicalHistoryUpdate,
)


def create_medical_history_service(
    db: Session,
    *,
    user_id: uuid.UUID,
    payload: MedicalHistoryCreate,
) -> MedicalHistory:
    existing_history = get_medical_history_by_user_id(
        db,
        user_id=user_id,
    )

    if existing_history:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Medical history already exists",
        )

    medical_history = MedicalHistory(
        user_id=user_id,
        chronic_conditions=payload.chronic_conditions,
        past_surgeries=payload.past_surgeries,
        family_history=payload.family_history,
    )

    return create_medical_history(
        db,
        medical_history=medical_history,
    )


def get_medical_history_service(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> MedicalHistory:
    medical_history = get_medical_history_by_user_id(
        db,
        user_id=user_id,
    )

    if not medical_history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medical history not found",
        )

    return medical_history


def update_medical_history_service(
    db: Session,
    *,
    user_id: uuid.UUID,
    payload: MedicalHistoryUpdate,
) -> MedicalHistory:
    medical_history = get_medical_history_by_user_id(
        db,
        user_id=user_id,
    )

    if not medical_history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medical history not found",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(medical_history, field, value)

    return update_medical_history(
        db,
        medical_history=medical_history,
    )