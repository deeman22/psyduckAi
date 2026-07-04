from fastapi import FastAPI

from backend.api.routes import router
from backend.core.event_bus import EventBus
from backend.context.context_manager import ContextManager
from backend.handlers.event_handler import EventHandler

app = FastAPI()

context = ContextManager("/Users/biswajitdas/my_proj/psyduckAi")
handler = EventHandler(context)

event_bus = EventBus()
event_bus.subscribe(handler.handle)

app.state.event_bus = event_bus

app.include_router(router)