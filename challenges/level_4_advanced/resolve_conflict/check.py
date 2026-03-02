"""Check: no MERGE_HEAD, no conflict markers, merge completed."""
from pathlib import Path

from challenges.base import is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    if (work_dir / ".git" / "MERGE_HEAD").exists():
        return False
    config = work_dir / "config.txt"
    if not config.exists():
        return False
    content = config.read_text()
    if "<<<<<<<" in content or "=======" in content or ">>>>>>>" in content:
        return False
    return True
