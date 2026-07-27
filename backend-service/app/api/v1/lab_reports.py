import uuid

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    Response,
    UploadFile,
    status,
)

from sqlalchemy.orm import Session

from app.api.deps import (
    get_db,
    get_current_user,
)

from app.models.user import User

from app.schemas.lab_reports import (
    LabReportResponse,
)

from app.services.lab_reports import (
    create_lab_report_service,
    get_lab_reports_service,
    get_lab_report_service,
    delete_lab_report_service,
)

router = APIRouter(
    prefix="/lab-reports",
    tags=["Lab Reports"],
)


@router.post(
    "",
    response_model=LabReportResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_lab_report(
    report_name: str = Form(...),
    report_type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_lab_report_service(
        db,
        user_id=current_user.id,
        report_name=report_name,
        report_type=report_type,
        file=file,
    )


@router.get(
    "",
    response_model=list[LabReportResponse],
)
def get_lab_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_lab_reports_service(
        db,
        user_id=current_user.id,
    )


@router.get(
    "/{report_id}",
    response_model=LabReportResponse,
)
def get_lab_report(
    report_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_lab_report_service(
        db,
        report_id=report_id,
        user_id=current_user.id,
    )


@router.delete(
    "/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_lab_report(
    report_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_lab_report_service(
        db,
        report_id=report_id,
        user_id=current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )

