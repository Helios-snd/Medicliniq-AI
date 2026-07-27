import uuid
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class MedicationCreate(BaseModel):
    medicine_name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: date | None = None
    notes: str | None = None


class MedicationUpdate(BaseModel):
    medicine_name: str | None = None
    dosage: str | None = None
    frequency: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    notes: str | None = None


class MedicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: uuid.UUID
    medicine_name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: date | None
    notes: str | None
    created_at: datetime
    updated_at: datetime

    