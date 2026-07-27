import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.allergies import Allergy

from app.repo.allergies import (
    get_allergies_by_user_id,
    get_allergy_by_id,
    create_allergy,
    update_allergy,
    delete_allergy,
)

from app.schemas.allergies import (
    AllergyCreate,
    AllergyUpdate,
)


def create_allergy_service(
    db: Session,
    *,
    user_id: uuid.UUID,
    payload: AllergyCreate,
) -> Allergy:

    allergy = Allergy(
        user_id=user_id,
        allergen=payload.allergen,
        reaction=payload.reaction,
        severity=payload.severity,
        notes=payload.notes,
    )

    return create_allergy(
        db,
        allergy=allergy,
    )


def get_allergies_service(
    db: Session,
    *,
    user_id: uuid.UUID,
):
    return get_allergies_by_user_id(
        db,
        user_id=user_id,
    )


def get_allergy_service(
    db: Session,
    *,
    allergy_id: uuid.UUID,
    user_id: uuid.UUID,
):
    allergy = get_allergy_by_id(
        db,
        allergy_id=allergy_id,
    )

    if not allergy or allergy.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Allergy not found",
        )

    return allergy


def update_allergy_service(
    db: Session,
    *,
    allergy_id: uuid.UUID,
    user_id: uuid.UUID,
    payload: AllergyUpdate,
):
    allergy = get_allergy_by_id(
        db,
        allergy_id=allergy_id,
    )

    if not allergy or allergy.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Allergy not found",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(allergy, field, value)

    return update_allergy(
        db,
        allergy=allergy,
    )


def delete_allergy_service(
    db: Session,
    *,
    allergy_id: uuid.UUID,
    user_id: uuid.UUID,
):
    allergy = get_allergy_by_id(
        db,
        allergy_id=allergy_id,
    )

    if not allergy or allergy.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Allergy not found",
        )

    delete_allergy(
        db,
        allergy=allergy,
    )

    