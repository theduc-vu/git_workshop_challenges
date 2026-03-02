"""Setup: repo with one commit that has a typo in message. Task: amend the message."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "doc.txt", "Some content.\n")
    run_git(work_dir, "add", "doc.txt")
    run_git(work_dir, "commit", "-m", "Inital commit")  # typo: Inital
    # Student should amend to e.g. "Initial commit"
