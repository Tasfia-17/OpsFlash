"""OpsFlash MCP Server - Governed Git automation via MCP"""
from fastmcp import FastMCP
from tools import branch, commit, merge, stash, safety

mcp = FastMCP("OpsFlash")

@mcp.tool()
def create_branch(branch_name: str, dry_run: bool = False) -> dict:
    """Create and checkout a new Git branch
    
    Args:
        branch_name: Name of the branch to create
        dry_run: If True, simulate the operation without executing
    """
    return branch.create_branch(branch_name, dry_run)

@mcp.tool()
def list_branches() -> dict:
    """List all local and remote Git branches"""
    return branch.list_branches()

@mcp.tool()
def safe_commit(message: str = None, auto_generate: bool = False, dry_run: bool = False) -> dict:
    """Stage changes and create a commit with optional AI-generated message
    
    Args:
        message: Commit message (optional if auto_generate is True)
        auto_generate: Generate commit message from staged changes
        dry_run: If True, simulate the operation without executing
    """
    return commit.safe_commit(message, auto_generate, dry_run)

@mcp.tool()
def merge_branch(source_branch: str, dry_run: bool = False) -> dict:
    """Merge source branch into current branch with safety checks
    
    Args:
        source_branch: Branch to merge from
        dry_run: If True, simulate the operation without executing
    """
    return merge.merge_branch(source_branch, dry_run)

@mcp.tool()
def stash_changes(apply_after: bool = False, dry_run: bool = False) -> dict:
    """Stash current changes with optional auto-apply
    
    Args:
        apply_after: If True, automatically pop the stash after stashing
        dry_run: If True, simulate the operation without executing
    """
    return stash.stash_changes(apply_after, dry_run)

@mcp.tool()
def validate_git_action(action_type: str, branch_name: str = None) -> dict:
    """Validate a Git action and return risk assessment
    
    Args:
        action_type: Type of Git action (e.g., 'merge', 'force_push', 'delete_branch')
        branch_name: Branch name for context-aware validation
    """
    return safety.validate_git_action(action_type, branch_name)

if __name__ == "__main__":
    mcp.run()
