"""Check: the previously 'lost' commit is reachable (e.g. branch points at it or HEAD does)."""
from pathlib import Path

from challenges.base import run_git, run_git_capture, is_git_repo


def check(work_dir: Path) -> bool:
    if not is_git_repo(work_dir):
        return False
    try:
        # Find commits in reflog that are not reachable from HEAD (the "lost" commits)
        reflog = run_git_capture(work_dir, "reflog", "--format=%H")
        head_sha = run_git_capture(work_dir, "rev-parse", "HEAD")
        lost_candidates = []
        for sha in reflog.splitlines():
            sha = sha.strip()
            if not sha or len(sha) != 40:
                continue
            if sha == head_sha:
                continue
            r = run_git(work_dir, "merge-base", "--is-ancestor", sha, "HEAD", check=False)
            if r.returncode != 0:
                lost_candidates.append(sha)
        if not lost_candidates:
            return False
        current_head = run_git_capture(work_dir, "rev-parse", "HEAD")
        for sha in lost_candidates:
            if current_head == sha:
                return True
            branches = run_git_capture(work_dir, "branch", "-a")
            for line in branches.splitlines():
                branch = line.strip().lstrip("* ")
                if not branch:
                    continue
                try:
                    tip = run_git_capture(work_dir, "rev-parse", branch)
                    if tip == sha:
                        return True
                except Exception:
                    continue
        return False
    except Exception:
        return False
