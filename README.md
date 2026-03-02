# Git Workshop Challenges

Self-contained git challenges for students: from brand new to professional git usage.

Prerequisites: **Python 3**, **pip** and **Git** are installed.

## Quick start

1. **Clone this repo**
   ```bash
   git clone <repo-url>
   cd git_workshop_challenges/
   ```

2. **Set up the virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows Powershell: venv\Scripts\Activate.ps1 / Cmd Prompt: venv\Scripts\activate.bat
   pip install -r requirements.txt
   ```

3. **Prepare challenge scenarios**
   ```bash
   python prepare.py
   ```
   This creates a `work/` folder with one directory per challenge, each a small git repo in the state you need to solve the challenge.

4. **Work on challenges**
   Go into each `work/<challenge_id>/` and follow the task. See [TASKS.md](TASKS.md) for the full list of tasks.

5. **Check your progress**
   ```bash
   python grade.py
   ```
   You'll see how many challenges you've completed (e.g. "Challenges completed: 3 / 13").

## Resetting a challenge

To reset a single challenge or all, run prepare again:
```bash
python prepare.py           # reset all
python prepare.py 06_merge_conflict   # reset only that one
```

## Challenge levels

- **Level 1 – Basics**: First commit, status/add, amend.
- **Level 2 – Branches**: Create branch, merge (no conflict), merge conflict.
- **Level 3 – Intermediate**: Remote tracking, pull/rebase, multi-user collaboration.
- **Level 4 – Advanced**: Detached HEAD, resolve conflict, reflog recovery, stash.

Requirements: Python 3.6+, Git.
