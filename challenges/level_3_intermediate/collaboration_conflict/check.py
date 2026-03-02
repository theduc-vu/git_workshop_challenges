"""Check: conflict resolved, merged, and pushed - no MERGE_HEAD, no conflict markers, in sync."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    if (work_dir / ".git" / "MERGE_HEAD").exists():
        return False
    report = work_dir / "report.txt"
    if not report.exists():
        return False
    content = report.read_text()
    if "<<<<<<<" in content or "=======" in content or ">>>>>>>" in content:
        return False
    try:
        run_git_capture(work_dir, "fetch", "origin")
        ahead = int(run_git_capture(work_dir, "rev-list", "--count", "origin/main..HEAD") or "0")
        behind = int(run_git_capture(work_dir, "rev-list", "--count", "HEAD..origin/main") or "0")
        return ahead == 0 and behind == 0
    except Exception:
        return False
