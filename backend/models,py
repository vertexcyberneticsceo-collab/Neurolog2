from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class AlertEvent(Base):
    __tablename__ = "alert_events"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    patient_id: Mapped[str] = mapped_column(String(128))
    device_id: Mapped[str] = mapped_column(String(128))

    started_at: Mapped[datetime] = mapped_column(DateTime)
    ended_at: Mapped[datetime] = mapped_column(DateTime)

    confidence: Mapped[float] = mapped_column(Float)
    reason: Mapped[str] = mapped_column(String(512))
