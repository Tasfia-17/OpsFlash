"""OpsFlash Core Logger - Structured logging for Git operations"""
import json
import logging
from datetime import datetime
from typing import Any, Dict

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("opsflash")

class OpsLogger:
    @staticmethod
    def log_action(action: str, details: Dict[str, Any], risk_level: str = "LOW"):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "risk_level": risk_level,
            "details": details
        }
        logger.info(json.dumps(log_entry, indent=2))
    
    @staticmethod
    def log_error(action: str, error: str):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "status": "ERROR",
            "error": error
        }
        logger.error(json.dumps(log_entry, indent=2))
