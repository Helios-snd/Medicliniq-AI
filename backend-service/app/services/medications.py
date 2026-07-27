import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.medications import Medication

from app.repo.medications import (
    get_medications_by_user_id,
    get_medication_by_id,
    create_medication,
    update_medication,
    delete_medication,
)

from app.schemas.medications import (
    MedicationCreate,
    MedicationUpdate,
)


def create_medication_service(db: Session, *, user_id: uuid.UUID, payload: MedicationCreate) -> Medication:

    medication = Medication(
        user_id=user_id,
        medicine_name=payload.medicine_name,
        dosage=payload.dosage,
        frequency=payload.frequency,
        start_date=payload.start_date,
        end_date=payload.end_date,
        notes=payload.notes,
    )

    return create_medication(
        db,
        medication=medication,
    )


def get_medications_service(db: Session, *, user_id: uuid.UUID) -> list[Medication]:

    return get_medications_by_user_id(
        db,
        user_id=user_id,
    )


def get_medication_service(db: Session, *, medication_id: uuid.UUID,user_id: uuid.UUID) -> Medication:

    medication = get_medication_by_id(db, medication_id=medication_id)

    if not medication:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medication not found",
        )

    if medication.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this medication",
        )

    return medication


def update_medication_service(db: Session, *, medication_id: uuid.UUID, user_id: uuid.UUID, payload: MedicationUpdate) -> Medication:

    medication = get_medication_by_id(
        db,
        medication_id=medication_id,
    )

    if not medication:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medication not found",
        )

    if medication.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this medication",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(medication, field, value)

    return update_medication(
        db,
        medication=medication,
    )


def delete_medication_service(db: Session, *, medication_id: uuid.UUID, user_id: uuid.UUID) -> None:

    medication = get_medication_by_id(
        db,
        medication_id=medication_id,
    )

    if not medication:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medication not found",
        )

    if medication.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this medication",
        )

    delete_medication(
        db,
        medication=medication,
    )

