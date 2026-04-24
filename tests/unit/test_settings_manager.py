"""Settings Manager Unit Tests"""

import pytest
import tempfile
from pathlib import Path
from services.settings_manager import SettingsManager


class TestSettingsManager:
    """Test settings manager functionality."""
    
    def test_initialization(self):
        """Test settings manager initialization."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SettingsManager(Path(tmpdir))
            assert manager.settings is not None
    
    def test_get_set_settings(self):
        """Test getting and setting values."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = SettingsManager(Path(tmpdir))
            
            manager.set("test_key", "test_value")
            assert manager.get("test_key") == "test_value"
    
    def test_default_settings(self):
        """Test default settings."""
        defaults = SettingsManager._get_default_settings()
        
        assert "theme" in defaults
        assert "hotkeys" in defaults
