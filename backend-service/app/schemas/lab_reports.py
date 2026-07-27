import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class LabReportCreate(BaseModel):
    report_name: str
    report_type: str


class LabReportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    user_id: uuid.UUID
    report_name: str
    report_type: str
    file_path: str
    processing_status: str
    created_at: datetime
    updated_at: datetime

