from pydantic import BaseModel
from datetime import datetime
from backend.models.event_type import EventType

class Event(BaseModel):
    type: EventType
    timestamp: datetime
    payload: dict