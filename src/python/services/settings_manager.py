"""Application Settings Management"""

import logging
import json
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)


class SettingsManager:
    """Manage application configuration and settings."""
    
    def __init__(self, config_dir: Path = None):
        self.config_dir = config_dir or Path.home() / ".hypixel_utility"
        self.config_file = self.config_dir / "config.json"
        self.settings: Dict[str, Any] = {}
        
        # Create config directory if needed
        self.config_dir.mkdir(exist_ok=True)
        
        # Load existing settings or create default
        self._load_settings()
    
    def _load_settings(self):
        """Load settings from file."""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    self.settings = json.load(f)
                logger.info(f"Loaded settings from {self.config_file}")
            else:
                self.settings = self._get_default_settings()
                self._save_settings()
        except Exception as e:
            logger.error(f"Failed to load settings: {e}")
            self.settings = self._get_default_settings()
    
    def _save_settings(self):
        """Save settings to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
            logger.info(f"Saved settings to {self.config_file}")
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a setting value."""
        self.settings[key] = value
        self._save_settings()
    
    def reset_to_default(self):
        """Reset all settings to default."""
        self.settings = self._get_default_settings()
        self._save_settings()
        logger.info("Settings reset to default")
    
    @staticmethod
    def _get_default_settings() -> Dict[str, Any]:
        """Get default settings."""
        return {
            "theme": "dark",
            "autostart": False,
            "auto_update": True,
            "cache_duration": 30,
            "hotkeys": {
                "toggle_window": "alt+shift+h",
                "autoclicker_start": "alt+a",
                "macro_start": "alt+m",
            }
        }
