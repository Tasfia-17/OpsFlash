"""OpsFlash Safety Validation Tools"""
from core.validator import Validator

def validate_git_action(action_type: str, branch_name: str = None) -> dict:
    """Validate a Git action and return risk assessment"""
    risk_level, requires_confirmation = Validator.validate_git_action(action_type, branch_name)
    
    return {
        "action_type": action_type,
        "branch_name": branch_name,
        "risk_level": risk_level,
        "requires_confirmation": requires_confirmation,
        "is_protected": Validator.is_protected_branch(branch_name) if branch_name else False
    }
