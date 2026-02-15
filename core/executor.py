"""OpsFlash Executor - Safe Git command execution wrapper"""
import subprocess
from typing import Dict, Any
from .logger import OpsLogger

class GitExecutor:
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
    
    def execute(self, command: list, action: str, risk_level: str = "LOW") -> Dict[str, Any]:
        """Execute git command with logging and dry-run support"""
        if self.dry_run:
            OpsLogger.log_action(action, {"command": " ".join(command), "dry_run": True}, risk_level)
            return {"status": "dry_run", "command": " ".join(command)}
        
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
            OpsLogger.log_action(action, {
                "command": " ".join(command),
                "output": result.stdout.strip()
            }, risk_level)
            return {"status": "success", "output": result.stdout.strip()}
        except subprocess.CalledProcessError as e:
            OpsLogger.log_error(action, e.stderr)
            return {"status": "error", "error": e.stderr}
