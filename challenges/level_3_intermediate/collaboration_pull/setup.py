"""Setup: you and another user have both pushed to the shared remote. Task: pull and merge, then push."""
import shutil
import subprocess
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    origin_bare = work_dir.parent / "12_collaboration_pull_origin.git"
    if origin_bare.exists():
        shutil.rmtree(origin_bare)
    create_repo(work_dir)
    write_file(work_dir, "shared.txt", "Initial\n")
    run_git(work_dir, "add", "shared.txt")
    run_git(work_dir, "commit", "-m", "Initial")
    subprocess.run(["git", "init", "--bare", str(origin_bare)], check=True, capture_output=True, cwd=work_dir)
    run_git(work_dir, "remote", "add", "origin", str(origin_bare))
    run_git(work_dir, "push", "-u", "origin", "main")
    # Your commit
    write_file(work_dir, "my_feature.txt", "My work\n")
    run_git(work_dir, "add", "my_feature.txt")
    run_git(work_dir, "commit", "-m", "My feature")
    # Other user pushes their commit
    clone_dir = work_dir.parent / "12_collaboration_pull_other"
    if clone_dir.exists():
        shutil.rmtree(clone_dir)
    subprocess.run(["git", "clone", str(origin_bare), str(clone_dir)], check=True, capture_output=True, cwd=work_dir.parent)
    run_git(clone_dir, "checkout", "-B", "main", "origin/main")
    write_file(clone_dir, "their_feature.txt", "Their work\n")
    run_git(clone_dir, "add", "their_feature.txt")
    run_git(clone_dir, "commit", "-m", "Their feature")
    run_git(clone_dir, "push", "origin", "main")
    shutil.rmtree(clone_dir)
    # State: you have my_feature.txt locally; origin has their_feature.txt. Divergent.
    # Task: pull (merge), then push.
