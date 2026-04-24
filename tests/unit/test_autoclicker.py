"""Autoclicker Unit Tests"""

import pytest
from core.autoclicker import Autoclicker


class TestAutoclicker:
    """Test autoclicker functionality."""
    
    def test_initialization(self):
        """Test autoclicker initialization."""
        clicker = Autoclicker()
        assert not clicker._running
    
    def test_invalid_cps(self):
        """Test invalid CPS values."""
        clicker = Autoclicker()
        
        with pytest.raises(ValueError):
            clicker.start(cps=25)  # Too high
        
        with pytest.raises(ValueError):
            clicker.start(cps=0)  # Too low
    
    def test_invalid_jitter(self):
        """Test invalid jitter values."""
        clicker = Autoclicker()
        
        with pytest.raises(ValueError):
            clicker.start(jitter=1.5)  # Too high
        
        with pytest.raises(ValueError):
            clicker.start(jitter=-0.1)  # Negative
    
    def test_invalid_mode(self):
        """Test invalid mode."""
        clicker = Autoclicker()
        
        with pytest.raises(ValueError):
            clicker.start(mode="invalid")
