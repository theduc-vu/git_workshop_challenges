#!/usr/bin/env python3
"""Grade challenges by checking work/ directory state. Reports X / Y completed."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    sys.path.insert(0, str(ROOT))
    from challenges.registry import get_challenges

    work_dir = ROOT / "work"
    challenges = get_challenges()
    completed = []
    not_completed = []
    missing = []

    for cid, name, level, _setup_fn, check_fn in challenges:
        target = work_dir / cid
        if not target.exists():
            missing.append((cid, name))
            continue
        try:
            if check_fn(target):
                completed.append((cid, name))
            else:
                not_completed.append((cid, name))
        except Exception as e:  # noqa: BLE001
            not_completed.append((cid, name))
            if "--verbose" in sys.argv or "-v" in sys.argv:
                print(f"Check failed for {cid}: {e}", file=sys.stderr)

    total = len(challenges)
    passed = len(completed)
    print(f"Challenges completed: {passed} / {total}")
    if completed:
        print("\nCompleted:")
        for cid, name in completed:
            print(f"  [x] {cid} - {name}")
    if not_completed:
        print("\nNot completed:")
        for cid, name in not_completed:
            print(f"  [ ] {cid} - {name}")
    if missing:
        print("\nNot prepared (run prepare.py first):")
        for cid, name in missing:
            print(f"  [ ] {cid} - {name}")


if __name__ == "__main__":
    main()
