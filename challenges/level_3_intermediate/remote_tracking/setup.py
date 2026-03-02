"""Setup: local repo with a commit and a local 'origin' bare repo. Task: push to origin."""
import shutil
import subprocess
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    origin_bare = work_dir.parent / "07_remote_tracking_origin.git"
    if origin_bare.exists():
        shutil.rmtree(origin_bare)
    create_repo(work_dir)
    write_file(work_dir, "hello.txt", "Push me to origin.\n")
    run_git(work_dir, "add", "hello.txt")
    run_git(work_dir, "commit", "-m", "Ready to push")
    subprocess.run(["git", "init", "--bare", str(origin_bare)], check=True, capture_output=True, cwd=work_dir)
    run_git(work_dir, "remote", "add", "origin", str(origin_bare))
    # Student must: git push -u origin main
