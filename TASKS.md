# Challenge Tasks

After running `python prepare.py`, each `work/<id>/` directory contains a git repo in a specific state. Your task is to fix or complete the scenario using git commands.

## Level 1 – Basics

### 01_first_commit
**State**: Empty repo with two untracked files: `file.txt` and `newfile.txt`.  
**Task**: Add and commit both files (make at least 2 commits).

### 02_amend_commit
**State**: One commit with a typo in the message ("Inital" instead of "Initial").  
**Task**: Amend the last commit to fix the message.

---

## Level 2 – Branches

### 03_create_branch
**State**: One commit on `main`.  
**Task**: Create a branch named `feature` and make at least one commit on it.

### 04_merge_no_conflict
**State**: `main` and `dev` have different files; you're on `main`.  
**Task**: Merge `dev` into `main`.

### 05_merge_conflict
**State**: `main` and `feature` both changed `story.txt`; merge is in progress with conflicts.  
**Task**: Resolve the conflict in `story.txt` and complete the merge.

---

## Level 3 – Intermediate

### 06_remote_tracking
**State**: Local repo with a commit; a bare "origin" remote is configured but not pushed.  
**Task**: Push `main` to `origin` and set upstream tracking.

### 07_pull_rebase
**State**: Local `main` and `origin/main` have diverged (different commits).  
**Task**: Run `git pull --rebase origin main` to rebase your local commits on top of the remote.

### 12_collaboration_pull
**State**: You and another user have both pushed to the shared remote. You have `my_feature.txt` locally; the remote has `their_feature.txt`.  
**Task**: Pull (merge), then push so both changes are on the remote.

### 13_collaboration_conflict
**State**: You and another user both modified `report.txt` differently. You committed "Status: Draft"; they pushed "Author: Alice".  
**Task**: Pull, resolve the conflict in `report.txt`, and push.

---

## Level 4 – Advanced

### 08_detached_head
**State**: HEAD is detached (you checked out a tag).  
**Task**: Get back onto a branch (e.g. `main`).

### 09_resolve_conflict
**State**: Merge in progress with conflict in `config.txt`.  
**Task**: Resolve the conflict and complete the merge.

### 10_reflog_recover
**State**: A commit was "lost" after a `git reset --hard`.  
**Task**: Use `git reflog` to find the lost commit and recover it (e.g. create a branch pointing at it).

### 11_stash_and_pop
**State**: Uncommitted changes on `main`; branch `other` exists.  
**Task**: Stash your changes, switch to `other`, and pop the stash so the changes appear on `other`.
