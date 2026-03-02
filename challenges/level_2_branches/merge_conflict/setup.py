"""Setup: main and branch 'feature' both change the same line in same file. Task: merge and resolve conflict."""
from pathlib import Path

from challenges.base import create_repo, write_file, run_git


def setup(work_dir: Path) -> None:
    create_repo(work_dir)
    write_file(work_dir, "story.txt", "Once upon a time.\n")
    run_git(work_dir, "add", "story.txt")
    run_git(work_dir, "commit", "-m", "Initial story")
    run_git(work_dir, "checkout", "-b", "feature")
    write_file(work_dir, "story.txt", "Once upon a time there was a dragon.\n")
    run_git(work_dir, "add", "story.txt")
    run_git(work_dir, "commit", "-m", "Add dragon")
    run_git(work_dir, "checkout", "main")
    write_file(work_dir, "story.txt", "Once upon a time there was a princess.\n")
    run_git(work_dir, "add", "story.txt")
    run_git(work_dir, "commit", "-m", "Add princess")
    # Student must: git merge feature, resolve conflict in story.txt, commit
    # Merge exits 1 when there's a conflict; repo is left in merge-in-progress state
    run_git(work_dir, "merge", "feature", "--no-edit", "--no-commit", "--no-ff", check=False)
