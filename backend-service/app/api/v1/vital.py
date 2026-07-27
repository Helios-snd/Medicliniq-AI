import uuid

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from sqlalchemy.orm import Session

from app.api.deps import (
    get_db,
    get_current_user,
)

from app.models.user import User

from app.schemas.vital import (
    VitalCreate,
    VitalUpdate,
    VitalResponse,
)

from app.services.vital import (
    create_vital_service,
    get_vitals_service,
    get_vital_service,
    update_vital_service,
    delete_vital_service,
)

router = APIRouter(
    prefix="/vitals",
    tags=["Vitals"],
)


@router.post(
    "",
    response_model=VitalResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_vital(
    payload: VitalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_vital_service(
        db,
        user_id=current_user.id,
        payload=payload,
    )


@router.get(
    "",
    response_model=list[VitalResponse],
)
def get_vitals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_vitals_service(
        db,
        user_id=current_user.id,
    )


@router.get(
    "/{vital_id}",
    response_model=VitalResponse,
)
def get_vital(
    vital_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_vital_service(
        db,
        vital_id=vital_id,
        user_id=current_user.id,
    )


@router.put(
    "/{vital_id}",
    response_model=VitalResponse,
)
def update_vital(
    vital_id: uuid.UUID,
    payload: VitalUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_vital_service(
        db,
        vital_id=vital_id,
        user_id=current_user.id,
        payload=payload,
    )


@router.delete(
    "/{vital_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_vital(
    vital_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_vital_service(
        db,
        vital_id=vital_id,
        user_id=current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )