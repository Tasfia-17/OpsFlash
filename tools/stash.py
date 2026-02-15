"""OpsFlash Stash Operations"""
from core.executor import GitExecutor
from core.validator import Validator

def stash_changes(apply_after: bool = False, dry_run: bool = False) -> dict:
    """Stash current changes with optional auto-apply"""
    executor = GitExecutor(dry_run)
    risk_level, _ = Validator.validate_git_action("stash")
    
    # Stash
    result = executor.execute(
        ["git", "stash"],
        "stash_changes",
        risk_level
    )
    
    if apply_after and result["status"] == "success":
        return executor.execute(
            ["git", "stash", "pop"],
            "stash_pop",
            risk_level
        )
    
    return result
