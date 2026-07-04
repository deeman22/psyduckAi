from typing import Callable

from backend.models.event import Event


class EventBus:

    def __init__(self):
        self.subscribers: list[Callable[[Event], None]] = []

    def subscribe(self, handler):
        self.subscribers.append(handler)

    def publish(self, event: Event):
        for handler in self.subscribers:
            handler(event)