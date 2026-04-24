"""Settings Data Model"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class AppSettings:
    """Application settings."""
    theme: str = "dark"
    autostart: bool = False
    auto_update: bool = True
    cache_duration: int = 30
    hotkeys: Dict[str, str] = field(default_factory=lambda: {
        "toggle_window": "alt+shift+h",
        "autoclicker_start": "alt+a",
        "macro_start": "alt+m",
    })
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "theme": self.theme,
            "autostart": self.autostart,
            "auto_update": self.auto_update,
            "cache_duration": self.cache_duration,
            "hotkeys": self.hotkeys,
        }
