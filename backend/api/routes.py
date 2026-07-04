from fastapi import APIRouter, Request

from backend.models.event import Event

router = APIRouter()


@router.post("/event")
def receive_event(event: Event, request: Request):

    request.app.state.event_bus.publish(event)

    return {"status": "ok"}