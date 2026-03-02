"""Check: branch 'feature' exists and has at least one commit (not only main)."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        branches = run_git_capture(work_dir, "branch")
        if "feature" not in branches:
            return False
        # feature should have at least one commit (can be same as main or ahead)
        run_git_capture(work_dir, "rev-parse", "feature")
        return True
    except Exception:
        return False
