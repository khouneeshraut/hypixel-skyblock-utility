"""Configuration Loader"""

import json
from pathlib import Path
from typing import Dict, Any


def load_config() -> Dict[str, Any]:
    """Load application configuration."""
    config_paths = [
        Path("config/default_config.json"),
        Path.home() / ".hypixel_utility/config.json",
    ]
    
    config = get_default_config()
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                    config.update(user_config)
                break
            except json.JSONDecodeError:
                continue
    
    return config


def get_default_config() -> Dict[str, Any]:
    """Get default configuration."""
    return {
        "app_name": "Hypixel SkyBlock Utility",
        "version": "0.1.0",
        "theme": "dark",
        "autostart": False,
        "api": {
            "cache_duration": 30,
            "timeout": 10,
        },
        "autoclicker": {
            "default_cps": 8,
            "max_cps": 20,
        },
    }
