import uuid

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.schemas.doctor import (
    DoctorCreate,
    DoctorUpdate,
    DoctorResponse,
)

from app.services.doctor import (
    create_doctor_service,
    get_doctors_service,
    get_doctor_service,
    update_doctor_service,
    delete_doctor_service,
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"],
)


@router.post(
    "",
    response_model=DoctorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_doctor(
    payload: DoctorCreate,
    db: Session = Depends(get_db),
):
    return create_doctor_service(
        db,
        payload=payload,
    )


@router.get(
    "",
    response_model=list[DoctorResponse],
)
def get_doctors(
    db: Session = Depends(get_db),
):
    return get_doctors_service(
        db,
    )


@router.get(
    "/{doctor_id}",
    response_model=DoctorResponse,
)
def get_doctor(
    doctor_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return get_doctor_service(
        db,
        doctor_id=doctor_id,
    )


@router.put(
    "/{doctor_id}",
    response_model=DoctorResponse,
)
def update_doctor(
    doctor_id: uuid.UUID,
    payload: DoctorUpdate,
    db: Session = Depends(get_db),
):
    return update_doctor_service(
        db,
        doctor_id=doctor_id,
        payload=payload,
    )


@router.delete(
    "/{doctor_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_doctor(
    doctor_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    delete_doctor_service(
        db,
        doctor_id=doctor_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )