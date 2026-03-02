"""Setup: repo on main with one commit. Task: create a branch named 'feature' and make a commit on it."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "main.txt", "On main.\n")
    run_git(work_dir, "add", "main.txt")
    run_git(work_dir, "commit", "-m", "First commit on main")
    # Student must: git checkout -b feature, add a file or change, commit
