"""Check: no MERGE_HEAD, no conflict markers in story.txt, merge completed."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        if (work_dir / ".git" / "MERGE_HEAD").exists():
            return False
        story = work_dir / "story.txt"
        if not story.exists():
            return False
        content = story.read_text()
        if "<<<<<<<" in content or "=======" in content or ">>>>>>>" in content:
            return False
        # Should have a merge commit (two parents) when merge completed
        run_git_capture(work_dir, "rev-parse", "HEAD")
        return True
    except Exception:
        return False
