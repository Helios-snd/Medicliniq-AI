import uuid

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user

from app.models.user import User

from app.schemas.medications import (
    MedicationCreate,
    MedicationUpdate,
    MedicationResponse,
)

from app.services.medications import (
    create_medication_service,
    get_medications_service,
    get_medication_service,
    update_medication_service,
    delete_medication_service,
)

router = APIRouter(
    prefix="/medications",
    tags=["Medications"],
)


@router.post(
    "",
    response_model=MedicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_medication(
    payload: MedicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_medication_service(
        db,
        user_id=current_user.id,
        payload=payload,
    )


@router.get(
    "",
    response_model=list[MedicationResponse],
)
def get_medications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_medications_service(
        db,
        user_id=current_user.id,
    )


@router.get(
    "/{medication_id}",
    response_model=MedicationResponse,
)
def get_medication(
    medication_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_medication_service(
        db,
        medication_id=medication_id,
        user_id=current_user.id,
    )


@router.put(
    "/{medication_id}",
    response_model=MedicationResponse,
)
def update_medication(
    medication_id: uuid.UUID,
    payload: MedicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_medication_service(
        db,
        medication_id=medication_id,
        user_id=current_user.id,
        payload=payload,
    )


@router.delete(
    "/{medication_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_medication(
    medication_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_medication_service(
        db,
        medication_id=medication_id,
        user_id=current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )