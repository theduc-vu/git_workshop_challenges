"""Check: pull --rebase was done: origin/main is ancestor of HEAD, and both b.txt and c.txt exist."""
from pathlib import Path

from challenges.base import run_git, run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        run_git(work_dir, "fetch", "origin", check=True)
        # origin/main should be ancestor of HEAD (we rebased local on top of remote)
        r = run_git(work_dir, "merge-base", "--is-ancestor", "origin/main", "HEAD", check=False)
        if r.returncode != 0:
            return False
        if not (work_dir / "b.txt").exists() or not (work_dir / "c.txt").exists():
            return False
        return True
    except Exception:
        return False
