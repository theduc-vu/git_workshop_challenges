"""Setup: uncommitted change on main. Task: stash, switch to branch 'other', pop stash."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "main.txt", "On main\n")
    run_git(work_dir, "add", "main.txt")
    run_git(work_dir, "commit", "-m", "Initial")
    run_git(work_dir, "checkout", "-b", "other")
    write_file(work_dir, "main.txt", "On main\n\nUncommitted change\n")
    run_git(work_dir, "checkout", "main")
    # Now main has uncommitted change in main.txt; branch other exists.
    # Student must: stash, checkout other, stash pop (so other has the change)
    # We leave the change in working tree on main.
    write_file(work_dir, "main.txt", "On main\n\nUncommitted change\n")
    # So state: we're on main, main.txt is modified (not staged). other branch exists.
    # Student: git stash, git checkout other, git stash pop. Success = other has the extra lines.