import subprocess


class GitObserver:

    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def _run_git_command(self, command: list[str]) -> str:
        result = subprocess.run(
            command,
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise Exception(result.stderr)

        return result.stdout.strip()

    def get_current_branch(self) -> str:
        return self._run_git_command(
            ["git", "branch", "--show-current"]
        )

    def get_recent_commits(self, limit: int = 5) -> list[str]:
        output = self._run_git_command(
            ["git", "log", f"-{limit}", "--oneline"]
        )
        return output.splitlines()

    def get_working_tree_summary(self) -> str:
        return self._run_git_command(
            ["git", "diff", "--stat"]
        )

    def get_changed_files(self) -> list[str]:
        output = self._run_git_command(
            ["git", "diff", "--name-only"]
        )
        return output.splitlines()

    def get_git_diff(self) -> str:
        return self._run_git_command(
            ["git", "diff", "--unified=3"]
        )
    
    def collect_context(self) -> dict:
        return {
            "branch": self.get_current_branch(),
            "recent_commits": self.get_recent_commits(),
            "changed_files": self.get_changed_files(),
            "diff_summary": self.get_working_tree_summary(),
            "diff": self.get_git_diff()
        }