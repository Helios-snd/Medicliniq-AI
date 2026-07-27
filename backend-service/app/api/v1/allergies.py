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

from app.schemas.allergies import (
    AllergyCreate,
    AllergyUpdate,
    AllergyResponse,
)

from app.services.allergies import (
    create_allergy_service,
    get_allergies_service,
    get_allergy_service,
    update_allergy_service,
    delete_allergy_service,
)

router = APIRouter(
    prefix="/allergies",
    tags=["Allergies"],
)


@router.post(
    "",
    response_model=AllergyResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_allergy(
    payload: AllergyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_allergy_service(
        db,
        user_id=current_user.id,
        payload=payload,
    )


@router.get(
    "",
    response_model=list[AllergyResponse],
)
def get_allergies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_allergies_service(
        db,
        user_id=current_user.id,
    )


@router.get(
    "/{allergy_id}",
    response_model=AllergyResponse,
)
def get_allergy(
    allergy_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_allergy_service(
        db,
        allergy_id=allergy_id,
        user_id=current_user.id,
    )


@router.put(
    "/{allergy_id}",
    response_model=AllergyResponse,
)
def update_allergy(
    allergy_id: uuid.UUID,
    payload: AllergyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_allergy_service(
        db,
        allergy_id=allergy_id,
        user_id=current_user.id,
        payload=payload,
    )


@router.delete(
    "/{allergy_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_allergy(
    allergy_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_allergy_service(
        db,
        allergy_id=allergy_id,
        user_id=current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )