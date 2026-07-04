from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class SessionMemory:
    current_task: str | None = None
    current_branch: str | None = None

    open_files: set[str] = field(default_factory=set)

    recent_events: list[dict] = field(default_factory=list)

    recent_errors: list[str] = field(default_factory=list)

    last_updated: datetime = field(default_factory=datetime.now)

    def add_open_file(self, file_name: str):
        self.open_files.add(file_name)
        self.touch()

    def add_error(self, error: str):
        self.recent_errors.append(error)

        if len(self.recent_errors) > 20:
            self.recent_errors.pop(0)

        self.touch()

    def add_event(self, event: dict):
        self.recent_events.append(event)

        if len(self.recent_events) > 100:
            self.recent_events.pop(0)

        self.touch()

    def touch(self):
        self.last_updated = datetime.now()