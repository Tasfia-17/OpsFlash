"""OpsFlash Branch Operations"""
from core.executor import GitExecutor
from core.validator import Validator

def create_branch(branch_name: str, dry_run: bool = False) -> dict:
    """Create and checkout a new Git branch"""
    executor = GitExecutor(dry_run)
    risk_level, _ = Validator.validate_git_action("create_branch")
    
    return executor.execute(
        ["git", "checkout", "-b", branch_name],
        f"create_branch: {branch_name}",
        risk_level
    )

def list_branches() -> dict:
    """List all local and remote branches"""
    executor = GitExecutor(dry_run=False)
    result = executor.execute(
        ["git", "branch", "-a"],
        "list_branches",
        "LOW"
    )
    return result
