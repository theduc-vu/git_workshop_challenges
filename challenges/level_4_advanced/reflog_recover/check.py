"""Check: the previously 'lost' commit (WIP - will reset) is reachable from HEAD or any branch."""
from pathlib import Path

from challenges.base import run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        # The lost commit has message "WIP - will reset". If it's reachable from any ref, it's recovered.
        log = run_git_capture(work_dir, "log", "--all", "--grep=WIP - will reset", "--oneline")
        return bool(log.strip())
    except Exception:
        return False
