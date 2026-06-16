from fastapi import FastAPI

app = FastAPI(title="Neurolog")


@app.get("/")
def root():
    return {
        "name": "Neurolog",
        "status": "running",
        "message": "Medical event monitoring API"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from detector import detect_possible_event
from models import AlertEvent
from schemas import IngestRequest

app = FastAPI(title="Neurolog")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "name": "Neurolog",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post("/ingest")
def ingest(payload: IngestRequest, db: Session = Depends(get_db)):
    if not payload.samples:
        raise HTTPException(status_code=400, detail="samples cannot be empty")

    detected, confidence, reason = detect_possible_event(payload.samples)

    if not detected:
        return {
            "detected": False,
            "confidence": confidence,
            "reason": reason,
        }

    event = AlertEvent(
        patient_id=payload.patient_id,
        device_id=payload.device_id,
        started_at=payload.samples[0].timestamp,
        ended_at=payload.samples[-1].timestamp,
        confidence=confidence,
        reason=reason,
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "detected": True,
        "event_id": event.id,
        "patient_id": event.patient_id,
        "device_id": event.device_id,
        "confidence": event.confidence,
        "reason": event.reason,
        "started_at": event.started_at,
        "ended_at": event.ended_at,
    }


@app.get("/events")
def list_events(db: Session = Depends(get_db)):
    events = db.query(AlertEvent).order_by(AlertEvent.started_at.desc()).all()

    return [
        {
            "id": event.id,
            "patient_id": event.patient_id,
            "device_id": event.device_id,
            "started_at": event.started_at,
            "ended_at": event.ended_at,
            "confidence": event.confidence,
            "reason": event.reason,
        }
        for event in events
    ]
