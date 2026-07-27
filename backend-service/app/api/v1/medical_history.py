from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.user import User

from app.schemas.medical_history import (
    MedicalHistoryCreate,
    MedicalHistoryUpdate,
    MedicalHistoryResponse,
)

from app.services.medical_history import (
    create_medical_history_service,
    get_medical_history_service,
    update_medical_history_service,
)

router = APIRouter(
    prefix="/medical-history",
    tags=["Medical History"],
)


@router.post(
    "",
    response_model=MedicalHistoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_medical_history(
    payload: MedicalHistoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_medical_history_service(
        db,
        user_id=current_user.id,
        payload=payload,
    )


@router.get(
    "/me",
    response_model=MedicalHistoryResponse,
)
def get_my_medical_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_medical_history_service(
        db,
        user_id=current_user.id,
    )


@router.put(
    "/me",
    response_model=MedicalHistoryResponse,
)
def update_my_medical_history(
    payload: MedicalHistoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_medical_history_service(
        db,
        user_id=current_user.id,
        payload=payload,
    )


