"""Check: origin has been pushed (bare repo has refs/heads/main)."""
from pathlib import Path


def check(work_dir: Path) -> bool:
    origin_bare = work_dir.parent / "07_remote_tracking_origin.git"
    ref = origin_bare / "refs" / "heads" / "main"
    return ref.exists() and len(ref.read_text().strip()) == 40
