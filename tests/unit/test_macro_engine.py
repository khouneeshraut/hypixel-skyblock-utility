"""Macro Engine Unit Tests"""

import pytest
from core.macro_engine import MacroEngine, MacroEvent


class TestMacroEngine:
    """Test macro engine functionality."""
    
    def test_initialization(self):
        """Test macro engine initialization."""
        engine = MacroEngine()
        assert not engine._recording
        assert not engine._playing
        assert len(engine._events) == 0
    
    def test_macro_event_creation(self):
        """Test macro event creation."""
        event = MacroEvent(
            event_type="key_press",
            timestamp=0.0,
            key="a"
        )
        
        assert event.event_type == "key_press"
        assert event.key == "a"
