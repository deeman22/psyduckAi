from backend.models.event import Event, EventType
from backend.models.project_context import ProjectContext
from backend.models.git_context import GitContext
from backend.observers.git_observer import GitObserver


class ContextManager:

    def __init__(self, repo_path: str):
        self.git_observer = GitObserver(repo_path)

    def build_context(self, event: Event) -> ProjectContext:

        context = ProjectContext()

        if event.type == EventType.GIT_CHANGE:
            context.git = GitContext(
                current_branch=self.git_observer.get_current_branch(),
                recent_commits=self.git_observer.get_recent_commits(),
                changed_files=self.git_observer.get_changed_files(),
                diff_summary=self.git_observer.get_working_tree_summary(),
                diff=self.git_observer.get_git_diff()
            )
            
            return context