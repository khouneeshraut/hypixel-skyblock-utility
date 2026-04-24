"""Bazaar API Unit Tests"""

import pytest
from services.bazaar_api import BazaarAPI


class TestBazaarAPI:
    """Test Bazaar API functionality."""
    
    def test_initialization(self):
        """Test API initialization."""
        api = BazaarAPI()
        assert api.BASE_URL == "https://api.hypixel.net/skyblock/bazaar"
    
    def test_cache_system(self):
        """Test caching system."""
        api = BazaarAPI()
        
        # Test cache validation
        assert not api._is_cache_valid("nonexistent")
