"""Setup: merge in progress with conflict in one file. Task: resolve and complete merge."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "config.txt", "version=1\n")
    run_git(work_dir, "add", "config.txt")
    run_git(work_dir, "commit", "-m", "Initial")
    run_git(work_dir, "checkout", "-b", "feature")
    write_file(work_dir, "config.txt", "version=1\nfeature=enabled\n")
    run_git(work_dir, "add", "config.txt")
    run_git(work_dir, "commit", "-m", "Enable feature")
    run_git(work_dir, "checkout", "main")
    write_file(work_dir, "config.txt", "version=2\n")
    run_git(work_dir, "add", "config.txt")
    run_git(work_dir, "commit", "-m", "Bump version")
    # Merge exits 1 when there's a conflict; repo is left in merge-in-progress state
    run_git(work_dir, "merge", "feature", "--no-edit", "--no-commit", "--no-ff", check=False)
