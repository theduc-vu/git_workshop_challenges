"""Central registry of all challenges: id, name, level, setup_func, check_func."""
from pathlib import Path
from typing import Callable, List, Tuple

# Challenge record: (id, name, level, setup, check)
Challenge = Tuple[str, str, str, Callable[[Path], None], Callable[[Path], bool]]


def _load_challenges() -> List[Challenge]:
    from challenges.level_1_basics.first_commit.setup import setup as setup_01
    from challenges.level_1_basics.first_commit.check import check as check_01
    from challenges.level_1_basics.amend_commit.setup import setup as setup_02
    from challenges.level_1_basics.amend_commit.check import check as check_02
    from challenges.level_2_branches.create_branch.setup import setup as setup_03
    from challenges.level_2_branches.create_branch.check import check as check_03
    from challenges.level_2_branches.merge_no_conflict.setup import setup as setup_04
    from challenges.level_2_branches.merge_no_conflict.check import check as check_04
    from challenges.level_2_branches.merge_conflict.setup import setup as setup_05
    from challenges.level_2_branches.merge_conflict.check import check as check_05
    from challenges.level_3_intermediate.remote_tracking.setup import setup as setup_06
    from challenges.level_3_intermediate.remote_tracking.check import check as check_06
    from challenges.level_3_intermediate.pull_rebase.setup import setup as setup_07
    from challenges.level_3_intermediate.pull_rebase.check import check as check_07
    from challenges.level_4_advanced.detached_head.setup import setup as setup_08
    from challenges.level_4_advanced.detached_head.check import check as check_08
    from challenges.level_4_advanced.resolve_conflict.setup import setup as setup_09
    from challenges.level_4_advanced.resolve_conflict.check import check as check_09
    from challenges.level_4_advanced.reflog_recover.setup import setup as setup_10
    from challenges.level_4_advanced.reflog_recover.check import check as check_10
    from challenges.level_4_advanced.stash_and_pop.setup import setup as setup_11
    from challenges.level_4_advanced.stash_and_pop.check import check as check_11
    from challenges.level_3_intermediate.collaboration_pull.setup import setup as setup_12
    from challenges.level_3_intermediate.collaboration_pull.check import check as check_12
    from challenges.level_3_intermediate.collaboration_conflict.setup import setup as setup_13
    from challenges.level_3_intermediate.collaboration_conflict.check import check as check_13

    return [
        ("01_first_commit", "Add and commit", "level_1_basics", setup_01, check_01),
        ("02_amend_commit", "Amend commit", "level_1_basics", setup_02, check_02),
        ("03_create_branch", "Create branch", "level_2_branches", setup_03, check_03),
        ("04_merge_no_conflict", "Merge (no conflict)", "level_2_branches", setup_04, check_04),
        ("05_merge_conflict", "Merge conflict", "level_2_branches", setup_05, check_05),
        ("06_remote_tracking", "Remote tracking", "level_3_intermediate", setup_06, check_06),
        ("07_pull_rebase", "Pull rebase", "level_3_intermediate", setup_07, check_07),
        ("08_detached_head", "Detached HEAD", "level_4_advanced", setup_08, check_08),
        ("09_resolve_conflict", "Resolve conflict", "level_4_advanced", setup_09, check_09),
        ("10_reflog_recover", "Reflog recover", "level_4_advanced", setup_10, check_10),
        ("11_stash_and_pop", "Stash and pop", "level_4_advanced", setup_11, check_11),
        ("12_collaboration_pull", "Collaboration: pull and push", "level_3_intermediate", setup_12, check_12),
        ("13_collaboration_conflict", "Collaboration: resolve and push", "level_3_intermediate", setup_13, check_13),
    ]


def get_challenges() -> List[Challenge]:
    return _load_challenges()
