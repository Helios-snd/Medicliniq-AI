import uuid

from fastapi import (
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.models.vital import Vital

from app.schemas.vital import (
    VitalCreate,
    VitalUpdate,
)

from app.repo.vital import (
    create_vital,
    get_vitals_by_user_id,
    get_vital_by_id,
    update_vital,
    delete_vital,
)


def create_vital_service(
    db: Session,
    *,
    user_id: uuid.UUID,
    payload: VitalCreate,
) -> Vital:

    vital = Vital(
        user_id=user_id,
        blood_pressure=payload.blood_pressure,
        heart_rate=payload.heart_rate,
        temperature=payload.temperature,
        oxygen_saturation=payload.oxygen_saturation,
        weight=payload.weight,
        height=payload.height,
    )

    return create_vital(
        db,
        vital=vital,
    )


def get_vitals_service(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> list[Vital]:

    return get_vitals_by_user_id(
        db,
        user_id=user_id,
    )


def get_vital_service(
    db: Session,
    *,
    vital_id: uuid.UUID,
    user_id: uuid.UUID,
) -> Vital:

    vital = get_vital_by_id(
        db,
        vital_id=vital_id,
    )

    if not vital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vital not found",
        )

    if vital.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    return vital


def update_vital_service(
    db: Session,
    *,
    vital_id: uuid.UUID,
    user_id: uuid.UUID,
    payload: VitalUpdate,
) -> Vital:

    vital = get_vital_by_id(
        db,
        vital_id=vital_id,
    )

    if not vital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vital not found",
        )

    if vital.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    for field, value in payload.model_dump(
        exclude_unset=True
    ).items():
        setattr(vital, field, value)

    return update_vital(
        db,
        vital=vital,
    )


def delete_vital_service(
    db: Session,
    *,
    vital_id: uuid.UUID,
    user_id: uuid.UUID,
) -> None:

    vital = get_vital_by_id(
        db,
        vital_id=vital_id,
    )

    if not vital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vital not found",
        )

    if vital.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    delete_vital(
        db,
        vital=vital,
    )