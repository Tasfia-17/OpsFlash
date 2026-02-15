"""OpsFlash Validator - Risk assessment for Git operations"""
from typing import Tuple

PROTECTED_BRANCHES = ["main", "master", "production", "prod"]

class Validator:
    @staticmethod
    def validate_git_action(action_type: str, branch_name: str = None) -> Tuple[str, bool]:
        """
        Returns: (risk_level, requires_confirmation)
        """
        if action_type == "force_push":
            return ("HIGH", True)
        
        if action_type == "delete_branch" and branch_name in PROTECTED_BRANCHES:
            return ("HIGH", True)
        
        if action_type == "merge" and branch_name in PROTECTED_BRANCHES:
            return ("MEDIUM", True)
        
        if action_type in ["commit", "create_branch", "stash"]:
            return ("LOW", False)
        
        return ("MEDIUM", False)
    
    @staticmethod
    def is_protected_branch(branch_name: str) -> bool:
        return branch_name in PROTECTED_BRANCHES
