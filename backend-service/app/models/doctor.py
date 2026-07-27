import uuid
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime, func, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base


class Doctor(Base): 
    __tablename__ = "Doctor"

    id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    specialization : Mapped[str] = mapped_column(String, nullable=False)
    hospital: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now(), nullable=False )

    