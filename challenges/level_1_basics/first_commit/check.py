"""Check: both file.txt and newfile.txt tracked, at least 2 commits."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        files = run_git_capture(work_dir, "ls-files")
        if "file.txt" not in files or "newfile.txt" not in files:
            return False
        count = run_git_capture(work_dir, "rev-list", "--count", "HEAD")
        return int(count) >= 2
    except (ValueError, FileNotFoundError):
        return False
