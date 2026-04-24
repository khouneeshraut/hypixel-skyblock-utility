"""Caching Service"""

import logging
from typing import Any, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class CacheManager:
    """Manage application-wide caching."""
    
    def __init__(self, default_ttl: int = 300):
        self._cache: dict = {}
        self._timestamps: dict = {}
        self.default_ttl = default_ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value."""
        if not self._is_valid(key):
            if key in self._cache:
                del self._cache[key]
                del self._timestamps[key]
            return None
        
        return self._cache.get(key)
    
    def set(self, key: str, value: Any, ttl: int = None):
        """Set cached value."""
        self._cache[key] = value
        self._timestamps[key] = datetime.now()
        logger.debug(f"Cached: {key}")
    
    def clear(self):
        """Clear all cache."""
        self._cache.clear()
        self._timestamps.clear()
        logger.info("Cache cleared")
    
    def _is_valid(self, key: str) -> bool:
        """Check if cache entry is still valid."""
        if key not in self._timestamps:
            return False
        
        age = datetime.now() - self._timestamps[key]
        return age < timedelta(seconds=self.default_ttl)
