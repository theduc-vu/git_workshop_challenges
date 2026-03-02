"""Check: HEAD is on a branch (git branch --show-current is non-empty)."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        branch = run_git_capture(work_dir, "branch", "--show-current")
        return len(branch) > 0
    except Exception:
        return False
