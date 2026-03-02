#!/usr/bin/env python3
"""Create or reset work/ and set up each challenge scenario."""
import argparse
import shutil
import sys
from pathlib import Path

# Project root (parent of script dir when run as script)
ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare git challenge scenarios in work/")
    parser.add_argument(
        "challenge",
        nargs="?",
        help="Optional: prepare only this challenge id (e.g. 06_merge_conflict). Otherwise all.",
    )
    parser.add_argument(
        "--no-reset",
        action="store_true",
        help="Skip existing work dirs (do not delete and recreate). Default is to reset.",
    )
    args = parser.parse_args()

    sys.path.insert(0, str(ROOT))
    from challenges.registry import get_challenges

    work_dir = ROOT / "work"
    work_dir.mkdir(parents=True, exist_ok=True)
    challenges = get_challenges()
    if args.challenge:
        challenges = [c for c in challenges if c[0] == args.challenge]
        if not challenges:
            print(f"Unknown challenge: {args.challenge}", file=sys.stderr)
            sys.exit(1)

    for cid, name, _level, setup_fn, _check_fn in challenges:
        target = work_dir / cid
        if target.exists():
            if args.no_reset:
                print(f"Skip (exists): {cid}")
                continue
            shutil.rmtree(target)
        target.mkdir(parents=True)
        print(f"Setup: {cid} - {name}")
        setup_fn(target)

    print("Done. Work directories are in work/")


if __name__ == "__main__":
    main()
