"""Check: pulled and pushed - origin has both my_feature.txt and their_feature.txt."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        run_git_capture(work_dir, "fetch", "origin")
        if not (work_dir / "my_feature.txt").exists():
            return False
        if not (work_dir / "their_feature.txt").exists():
            return False
        ahead = int(run_git_capture(work_dir, "rev-list", "--count", "origin/main..HEAD") or "0")
        behind = int(run_git_capture(work_dir, "rev-list", "--count", "HEAD..origin/main") or "0")
        return ahead == 0 and behind == 0
    except Exception:
        return False
