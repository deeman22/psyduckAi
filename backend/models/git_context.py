from pydantic import BaseModel

class GitContext(BaseModel):
    current_branch: str
    recent_commits: list[str]
    diff_summary: str