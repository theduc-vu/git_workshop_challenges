"""Setup: a 'lost' commit (reset --hard back). Task: recover it using reflog and point a branch at it."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git, run_git_capture


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "important.txt", "Do not lose this.\n")
    run_git(work_dir, "add", "important.txt")
    run_git(work_dir, "commit", "-m", "Important work")
    first_sha = run_git_capture(work_dir, "rev-parse", "HEAD")
    write_file(work_dir, "important.txt", "Do not lose this.\n\nExtra line\n")
    run_git(work_dir, "add", "important.txt")
    run_git(work_dir, "commit", "-m", "WIP - will reset")
    run_git(work_dir, "reset", "--hard", first_sha)
