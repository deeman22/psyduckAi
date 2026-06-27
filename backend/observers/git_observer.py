# observers/git_observer.py

import subprocess


class GitObserver:

    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def get_current_branch(self) -> str:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

observer = GitObserver("/Users/biswajitdas/my_proj/psyduckAi")

print(observer.get_current_branch())