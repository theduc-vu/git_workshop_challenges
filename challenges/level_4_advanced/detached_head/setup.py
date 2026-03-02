"""Setup: HEAD is detached (checkout a tag). Task: get back onto branch main."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "file.txt", "Content\n")
    run_git(work_dir, "add", "file.txt")
    run_git(work_dir, "commit", "-m", "First commit")
    run_git(work_dir, "tag", "v1.0")
    write_file(work_dir, "file.txt", "Content v2\n")
    run_git(work_dir, "add", "file.txt")
    run_git(work_dir, "commit", "-m", "Second commit")
    # Detach HEAD at the tag (first commit)
    run_git(work_dir, "checkout", "v1.0")
    # Student must: git checkout main (or create/checkout a branch so HEAD is on a branch)
