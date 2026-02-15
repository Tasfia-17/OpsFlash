"""OpsFlash Commit Operations"""
import subprocess
from core.executor import GitExecutor
from core.validator import Validator

def safe_commit(message: str = None, auto_generate: bool = False, dry_run: bool = False) -> dict:
    """Stage changes and commit with optional AI-generated message"""
    executor = GitExecutor(dry_run)
    risk_level, _ = Validator.validate_git_action("commit")
    
    # Stage all changes
    stage_result = executor.execute(
        ["git", "add", "-A"],
        "stage_changes",
        risk_level
    )
    
    if stage_result["status"] == "error":
        return stage_result
    
    # Generate message if needed
    if auto_generate and not message:
        message = _generate_commit_message()
    
    if not message:
        return {"status": "error", "error": "No commit message provided"}
    
    # Commit
    return executor.execute(
        ["git", "commit", "-m", message],
        f"commit: {message[:50]}",
        risk_level
    )

def _generate_commit_message() -> str:
    """Generate commit message from staged changes"""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--stat"],
            capture_output=True,
            text=True
        )
        stats = result.stdout.strip()
        if not stats:
            return "chore: update files"
        
        # Simple heuristic
        if "test" in stats.lower():
            return "test: add/update tests"
        elif "doc" in stats.lower() or "readme" in stats.lower():
            return "docs: update documentation"
        else:
            return "feat: implement changes"
    except:
        return "chore: update files"
