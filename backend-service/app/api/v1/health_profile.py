from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.user import User

from app.schemas.health_profile import (
    HealthProfileCreate,
    HealthProfileResponse,
    HealthProfileUpdate,
)

from app.services.health_profile import (
    create_profile,
    get_profile,
    update_profile,
)

router = APIRouter(prefix="/health-profile", tags=["Health Profile"])

@router.post(
    "",
    response_model=HealthProfileResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_health_profile_route(
    payload: HealthProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_profile(
        db,
        user_id=current_user.id,
        payload=payload,
    )


@router.get(
    "/me",
    response_model=HealthProfileResponse,
)
def get_my_health_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_profile(
        db,
        user_id=current_user.id,
    )


@router.put(
    "/me",
    response_model=HealthProfileResponse,
)
def update_my_health_profile(
    payload: HealthProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_profile(
        db,
        user_id=current_user.id,
        payload=payload,
    )