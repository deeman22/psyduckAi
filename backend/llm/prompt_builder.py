from backend.models.event import Event
from backend.models.project_context import ProjectContext


class PromptBuilder:

    def build(
        self,
        event: Event,
        context: ProjectContext
    ) -> str:

        prompt = f"""
You are PsyDuck.

Event:
{event.type.value}

"""

        if context.git:
            prompt += f"""

Git Context
-----------
Branch:
{context.git.current_branch}

Recent Commits:
{chr(10).join(context.git.recent_commits)}

Diff:
{context.git.diff_summary}
"""

        return prompt