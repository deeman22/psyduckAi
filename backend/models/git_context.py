from dataclasses import dataclass, field


@dataclass
class GitContext:

    current_branch: str = ""

    recent_commits: list[str] = field(default_factory=list)

    changed_files: list[str] = field(default_factory=list)

    diff_summary: str = ""

    diff: str = ""