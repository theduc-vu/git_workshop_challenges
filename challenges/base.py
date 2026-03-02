"""Shared helpers for challenge setup and checks."""
import subprocess
from pathlib import Path


def run_git(work_dir: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run git in work_dir. args are passed to git (e.g. 'status', '--short')."""
    cmd = ["git", *args]
    return subprocess.run(
        cmd,
        cwd=work_dir,
        capture_output=True,
        text=True,
        check=check,
    )


def run_git_capture(work_dir: Path, *args: str) -> str:
    """Run git in work_dir and return stripped stdout. Raises on non-zero exit."""
    r = run_git(work_dir, *args)
    return (r.stdout or "").strip()


def create_repo(work_dir: Path, default_branch: str = "main") -> None:
    """Create a fresh git repo in work_dir. work_dir must exist and be empty (or we init anyway)."""
    work_dir.mkdir(parents=True, exist_ok=True)
    run_git(work_dir, "init")
    run_git(work_dir, "branch", "-M", default_branch)


def write_file(work_dir: Path, path: str, content: str) -> Path:
    """Write content to work_dir/path. Creates parent dirs. Returns full path."""
    full = work_dir / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding="utf-8")
    return full


def is_git_repo(work_dir: Path) -> bool:
    """Return True if work_dir is a git repository."""
    if not work_dir.is_dir():
        return False
    return (work_dir / ".git").is_dir()
