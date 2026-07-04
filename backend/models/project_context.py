from pydantic import BaseModel

from backend.models.git_context import GitContext


class ProjectContext(BaseModel):
    git: GitContext | None = None