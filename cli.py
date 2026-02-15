#!/usr/bin/env python3
"""OpsFlash CLI - Test interface for OpsFlash MCP server"""
import sys
from tools import branch, commit, merge, stash, safety

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <command> [args]")
        print("\nCommands:")
        print("  create-branch <name> [--dry-run]")
        print("  list-branches")
        print("  commit <message> [--dry-run]")
        print("  merge <source> [--dry-run]")
        print("  stash [--apply-after] [--dry-run]")
        print("  validate <action> [branch]")
        sys.exit(1)
    
    command = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    
    if command == "create-branch":
        if len(sys.argv) < 3:
            print("Error: branch name required")
            sys.exit(1)
        result = branch.create_branch(sys.argv[2], dry_run)
        print(result)
    
    elif command == "list-branches":
        result = branch.list_branches()
        print(result)
    
    elif command == "commit":
        message = sys.argv[2] if len(sys.argv) > 2 else None
        result = commit.safe_commit(message, auto_generate=not message, dry_run=dry_run)
        print(result)
    
    elif command == "merge":
        if len(sys.argv) < 3:
            print("Error: source branch required")
            sys.exit(1)
        result = merge.merge_branch(sys.argv[2], dry_run)
        print(result)
    
    elif command == "stash":
        apply_after = "--apply-after" in sys.argv
        result = stash.stash_changes(apply_after, dry_run)
        print(result)
    
    elif command == "validate":
        if len(sys.argv) < 3:
            print("Error: action type required")
            sys.exit(1)
        action = sys.argv[2]
        branch_name = sys.argv[3] if len(sys.argv) > 3 else None
        result = safety.validate_git_action(action, branch_name)
        print(result)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
