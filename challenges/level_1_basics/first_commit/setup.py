"""Setup: repo with two untracked files. Task: add and commit both (make at least 2 commits)."""
from pathlib import Path

from challenges.base import create_repo, write_file


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "file.txt", "Hello, git!\n")
    write_file(work_dir, "newfile.txt", "Add this file with git add and commit.\n")
    # Both untracked; student must add and commit both (at least 2 commits).
