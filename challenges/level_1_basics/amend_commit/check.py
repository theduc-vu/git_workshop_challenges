"""Check: latest commit message does not contain the typo 'Inital'."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        msg = run_git_capture(work_dir, "log", "-1", "--format=%s")
        return "Inital" not in msg and len(msg) > 0
    except FileNotFoundError:
        return False
