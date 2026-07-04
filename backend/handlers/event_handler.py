from backend.models.event import Event, EventType
from backend.context.context_manager import ContextManager


class EventHandler:

    def __init__(self, context_manager: ContextManager):
        self.context = context_manager

    def handle(self, event: Event):

        if event.type == EventType.GIT_CHANGE:

            git_context = self.context.get_git_context()

            print(git_context)

        elif event.type == EventType.FILE_SAVED:

            print(event.payload)
