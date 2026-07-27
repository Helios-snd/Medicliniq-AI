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

from app.schemas.symptom import (
    SymptomCreate,
    SymptomUpdate,
    SymptomResponse,
)

from app.services.symptom import (
    create_symptom_service,
    get_symptoms_service,
    get_symptom_service,
    update_symptom_service,
    delete_symptom_service,
)

router = APIRouter(
    prefix="/symptoms",
    tags=["Symptoms"],
)


@router.post(
    "",
    response_model=SymptomResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_symptom(
    payload: SymptomCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_symptom_service(
        db,
        user_id=current_user.id,
        payload=payload,
    )


@router.get(
    "",
    response_model=list[SymptomResponse],
)
def get_symptoms(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_symptoms_service(
        db,
        user_id=current_user.id,
    )


@router.get(
    "/{symptom_id}",
    response_model=SymptomResponse,
)
def get_symptom(
    symptom_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_symptom_service(
        db,
        symptom_id=symptom_id,
        user_id=current_user.id,
    )


@router.put(
    "/{symptom_id}",
    response_model=SymptomResponse,
)
def update_symptom(
    symptom_id: uuid.UUID,
    payload: SymptomUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_symptom_service(
        db,
        symptom_id=symptom_id,
        user_id=current_user.id,
        payload=payload,
    )


@router.delete(
    "/{symptom_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_symptom(
    symptom_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_symptom_service(
        db,
        symptom_id=symptom_id,
        user_id=current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )