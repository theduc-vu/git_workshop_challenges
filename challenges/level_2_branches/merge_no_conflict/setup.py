"""Setup: main and branch 'dev' with different files. Task: merge dev into main."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "main_only.txt", "Main\n")
    run_git(work_dir, "add", "main_only.txt")
    run_git(work_dir, "commit", "-m", "Main commit")
    run_git(work_dir, "checkout", "-b", "dev")
    write_file(work_dir, "dev_only.txt", "Dev\n")
    run_git(work_dir, "add", "dev_only.txt")
    run_git(work_dir, "commit", "-m", "Dev commit")
    run_git(work_dir, "checkout", "main")
    # Student must: git merge dev (no conflict)
