import os
import uuid

from fastapi import (
    HTTPException,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

from app.models.lab_reports import LabReport

from app.repo.lab_reports import (
    create_lab_report,
    get_lab_reports_by_user_id,
    get_lab_report_by_id,
    delete_lab_report,
)


UPLOAD_DIR = "uploads/reports"


def create_lab_report_service(
    db: Session,
    *,
    user_id: uuid.UUID,
    report_name: str,
    report_type: str,
    file: UploadFile,
) -> LabReport:

    allowed_types = [
        "application/pdf",
        "image/jpeg",
        "image/png",
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF, JPG and PNG files are allowed",
        )

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True,
    )

    unique_filename = (
        f"{uuid.uuid4()}_{file.filename}"
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename,
    )

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    lab_report = LabReport(
        user_id=user_id,
        report_name=report_name,
        report_type=report_type,
        file_path=file_path,
        processing_status="pending",
    )

    return create_lab_report(
        db,
        lab_report=lab_report,
    )


def get_lab_reports_service(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> list[LabReport]:

    return get_lab_reports_by_user_id(
        db,
        user_id=user_id,
    )


def get_lab_report_service(
    db: Session,
    *,
    report_id: uuid.UUID,
    user_id: uuid.UUID,
) -> LabReport:

    report = get_lab_report_by_id(
        db,
        report_id=report_id,
    )

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lab report not found",
        )

    if report.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    return report


def delete_lab_report_service(
    db: Session,
    *,
    report_id: uuid.UUID,
    user_id: uuid.UUID,
) -> None:

    report = get_lab_report_by_id(
        db,
        report_id=report_id,
    )

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lab report not found",
        )

    if report.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    if os.path.exists(report.file_path):
        os.remove(report.file_path)

    delete_lab_report(
        db,
        lab_report=report,
    )

