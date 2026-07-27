import uuid
from sqlalchemy.orm import Session
from app.models.doctor import Doctor


def create_doctor(db:Session, *, doctor: Doctor)-> Doctor:
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def get_doctors(db:Session)-> list[Doctor]: return db.query(Doctor).all()


def get_doctor_by_id(db:Session, *, doctor_id: uuid.UUID)-> Doctor | None:
    return (
        db.query(Doctor).filter(Doctor.id == doctor_id).first()
    )


def update_doctor(db:Session, *, doctor: Doctor) -> Doctor:
    db.commit()
    db.refresh(doctor)
    return doctor


def delete_doctor(db:Session, *, doctor: Doctor) -> None:
    db.delete(doctor)
    db.commit()


