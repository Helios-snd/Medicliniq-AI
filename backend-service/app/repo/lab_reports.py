import uuid

from sqlalchemy.orm import Session

from app.models.lab_reports import LabReport


def create_lab_report(
    db: Session,
    *,
    lab_report: LabReport,
) -> LabReport:
    db.add(lab_report)
    db.commit()
    db.refresh(lab_report)

    return lab_report


def get_lab_reports_by_user_id(
    db: Session,
    *,
    user_id: uuid.UUID,
) -> list[LabReport]:
    return (
        db.query(LabReport)
        .filter(LabReport.user_id == user_id)
        .all()
    )


def get_lab_report_by_id(
    db: Session,
    *,
    report_id: uuid.UUID,
) -> LabReport | None:
    return (
        db.query(LabReport)
        .filter(LabReport.id == report_id)
        .first()
    )


def delete_lab_report(
    db: Session,
    *,
    lab_report: LabReport,
) -> None:
    db.delete(lab_report)
    db.commit()

    