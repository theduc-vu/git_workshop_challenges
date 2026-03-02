"""Setup: local main and 'origin' with divergent commits. Task: pull --rebase to update main."""
import shutil
import subprocess
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    origin_bare = work_dir.parent / "08_pull_rebase_origin.git"
    if origin_bare.exists():
        shutil.rmtree(origin_bare)
    create_repo(work_dir)
    write_file(work_dir, "a.txt", "First\n")
    run_git(work_dir, "add", "a.txt")
    run_git(work_dir, "commit", "-m", "First commit")
    subprocess.run(["git", "init", "--bare", str(origin_bare)], check=True, capture_output=True, cwd=work_dir)
    run_git(work_dir, "remote", "add", "origin", str(origin_bare))
    run_git(work_dir, "push", "-u", "origin", "main")
    # Add another commit locally (simulate divergence)
    write_file(work_dir, "b.txt", "Local\n")
    run_git(work_dir, "add", "b.txt")
    run_git(work_dir, "commit", "-m", "Local commit")
    # Add commit on "origin" by cloning bare, committing, pushing back
    clone_dir = work_dir.parent / "08_pull_rebase_origin_clone"
    if clone_dir.exists():
        shutil.rmtree(clone_dir)
    subprocess.run(["git", "clone", str(origin_bare), str(clone_dir)], check=True, capture_output=True, cwd=work_dir.parent)
    # Ensure clone is on main (clone may create master depending on git config)
    run_git(clone_dir, "checkout", "-B", "main", "origin/main")
    write_file(clone_dir, "c.txt", "Remote\n")
    run_git(clone_dir, "add", "c.txt")
    run_git(clone_dir, "commit", "-m", "Remote commit")
    run_git(clone_dir, "push", "origin", "main")
    shutil.rmtree(clone_dir)
    # Student must: git pull --rebase origin main (so local is on top of remote)
    # We do not pull; leave for student.
    # State: main has Local commit; origin/main has Remote commit. Divergent.
    # After pull --rebase: history is Remote then Local, and main has both.
    # Check: refs/remotes/origin/main is ancestor of HEAD, and b.txt and c.txt both exist.