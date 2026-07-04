from backend.observers.git_observer import GitObserver
from backend.models.git_context import GitContext

class ContextManager:

    def __init__(self, repo_path: str):
        self.git = GitObserver(repo_path)

    def get_git_context(self) -> GitContext:
        return GitContext(
            current_branch=self.git.get_current_branch(),
            recent_commits=self.git.get_recent_commits(),
            diff_summary=self.git.get_diff_summary()
        )