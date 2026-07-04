from fastapi import FastAPI

from backend.api.routes import router
from backend.core.event_bus import EventBus
from backend.context.context_manager import ContextManager
from backend.handlers.event_handler import EventHandler
from backend.llm.ollama_client import OllamaClient
from backend.core.config import settings


app = FastAPI()

# TODO: Replace this with the actual repository path.
repo_path = "/Users/biswajitdas/my_proj/psyduckAi"

context_manager = ContextManager(settings.repo_path)
llm = OllamaClient()

handler = EventHandler(
    context_manager=context_manager,
    llm=llm
)

event_bus = EventBus()
event_bus.subscribe(handler.handle)

app.state.event_bus = event_bus

app.include_router(router)