"""Setup: you and another user both modified the same file. Task: pull, resolve conflict, push."""
import shutil
import subprocess
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    origin_bare = work_dir.parent / "13_collaboration_conflict_origin.git"
    if origin_bare.exists():
        shutil.rmtree(origin_bare)
    create_repo(work_dir)
    write_file(work_dir, "report.txt", "Title: Q1 Report\n")
    run_git(work_dir, "add", "report.txt")
    run_git(work_dir, "commit", "-m", "Initial report")
    subprocess.run(["git", "init", "--bare", str(origin_bare)], check=True, capture_output=True, cwd=work_dir)
    run_git(work_dir, "remote", "add", "origin", str(origin_bare))
    run_git(work_dir, "push", "-u", "origin", "main")
    # Other user modifies report.txt and pushes
    clone_dir = work_dir.parent / "13_collaboration_conflict_other"
    if clone_dir.exists():
        shutil.rmtree(clone_dir)
    subprocess.run(["git", "clone", str(origin_bare), str(clone_dir)], check=True, capture_output=True, cwd=work_dir.parent)
    run_git(clone_dir, "checkout", "-B", "main", "origin/main")
    write_file(clone_dir, "report.txt", "Title: Q1 Report\nAuthor: Alice\n")
    run_git(clone_dir, "add", "report.txt")
    run_git(clone_dir, "commit", "-m", "Alice added author")
    run_git(clone_dir, "push", "origin", "main")
    shutil.rmtree(clone_dir)
    # You modify report.txt locally (different change)
    write_file(work_dir, "report.txt", "Title: Q1 Report\nStatus: Draft\n")
    run_git(work_dir, "add", "report.txt")
    run_git(work_dir, "commit", "-m", "I added status")
    # State: origin has "Author: Alice"; you have "Status: Draft". Same line area, conflict.
    # Task: pull, resolve conflict in report.txt, push.
