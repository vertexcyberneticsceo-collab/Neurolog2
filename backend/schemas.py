from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SensorSample(BaseModel):
    timestamp: datetime
    accel_x: float
    accel_y: float
    accel_z: float
    gyro_x: float
    gyro_y: float
    gyro_z: float
    heart_rate: Optional[int] = Field(default=None, ge=20, le=250)
    stress_level: Optional[float] = Field(default=None, ge=0, le=100)
    sleep_stage: Optional[str] = None
    walking_detected: bool = False


class IngestRequest(BaseModel):
    device_id: str
    patient_id: str
    samples: list[SensorSample]
