import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.doctor import Doctor

from app.repo.doctor import (
    create_doctor,
    get_doctors,
    get_doctor_by_id,
    update_doctor,
    delete_doctor,
)

from app.schemas.doctor import (
    DoctorCreate,
    DoctorUpdate,
)


def create_doctor_service(
    db: Session,
    *,
    payload: DoctorCreate,
) -> Doctor:
    doctor = Doctor(
        name=payload.name,
        specialization=payload.specialization,
        hospital=payload.hospital,
        phone_number=payload.phone_number,
        email=payload.email,
    )

    return create_doctor(
        db,
        doctor=doctor,
    )


def get_doctors_service(
    db: Session,
) -> list[Doctor]:
    return get_doctors(db)


def get_doctor_service(
    db: Session,
    *,
    doctor_id: uuid.UUID,
) -> Doctor:
    doctor = get_doctor_by_id(
        db,
        doctor_id=doctor_id,
    )

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found",
        )

    return doctor


def update_doctor_service(
    db: Session,
    *,
    doctor_id: uuid.UUID,
    payload: DoctorUpdate,
) -> Doctor:
    doctor = get_doctor_by_id(
        db,
        doctor_id=doctor_id,
    )

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found",
        )

    update_data = payload.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(doctor, field, value)

    return update_doctor(
        db,
        doctor=doctor,
    )


def delete_doctor_service(
    db: Session,
    *,
    doctor_id: uuid.UUID,
) -> None:
    doctor = get_doctor_by_id(
        db,
        doctor_id=doctor_id,
    )

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor not found",
        )

    delete_doctor(
        db,
        doctor=doctor,
    )