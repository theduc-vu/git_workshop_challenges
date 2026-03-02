"""Check: dev was merged into main (merge commit or main has dev's file)."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        # Either merge commit exists (two parents) or main has dev_only.txt
        if (work_dir / "dev_only.txt").read_text().strip() != "Dev":
            return False
        # We're on main and dev_only.txt is present (came from merge)
        branch = run_git_capture(work_dir, "branch", "--show-current")
        return branch == "main"
    except Exception:
        return False
