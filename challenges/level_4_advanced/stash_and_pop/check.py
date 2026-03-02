"""Check: branch 'other' has the stashed content (main.txt contains 'Uncommitted change')."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        # Committed on other
        content = run_git_capture(work_dir, "show", "other:main.txt")
        if "Uncommitted change" in content:
            return True
        # Or currently on other with change in working tree
        branch = run_git_capture(work_dir, "branch", "--show-current")
        if branch == "other" and (work_dir / "main.txt").exists():
            if "Uncommitted change" in (work_dir / "main.txt").read_text():
                return True
        return False
    except Exception:
        return False
