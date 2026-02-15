"""OpsFlash Merge Operations"""
import subprocess
from core.executor import GitExecutor
from core.validator import Validator

def merge_branch(source_branch: str, dry_run: bool = False) -> dict:
    """Merge source branch into current branch with safety checks"""
    # Get current branch
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True
        )
        current_branch = result.stdout.strip()
    except:
        return {"status": "error", "error": "Failed to get current branch"}
    
    # Validate
    risk_level, requires_confirmation = Validator.validate_git_action("merge", current_branch)
    
    if Validator.is_protected_branch(current_branch):
        return {
            "status": "blocked",
            "error": f"Cannot merge into protected branch: {current_branch}",
            "risk_level": "HIGH"
        }
    
    executor = GitExecutor(dry_run)
    return executor.execute(
        ["git", "merge", source_branch],
        f"merge: {source_branch} -> {current_branch}",
        risk_level
    )
