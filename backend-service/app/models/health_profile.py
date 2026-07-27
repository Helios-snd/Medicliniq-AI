import uuid
from datetime import date, datetime
from sqlalchemy import Date, DateTime, Float, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class HealthProfile(Base):
    __tablename__ = "health_profiles"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False,)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False,)
    gender: Mapped[str] = mapped_column(String(20), nullable=False,)
    blood_group: Mapped[str] = mapped_column(String(5), nullable=False,)
    height_cm: Mapped[float] = mapped_column(Float, nullable=False,)
    weight_kg: Mapped[float] = mapped_column(Float, nullable=False,)
    emergency_contact_name: Mapped[str | None] = mapped_column(String(255), nullable=True,)
    emergency_contact_number: Mapped[str | None] = mapped_column(String(20), nullable=True,)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False,)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False,)

