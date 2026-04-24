"""Input Handler Abstraction Layer"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class InputHandler:
    """Abstraction layer for input operations."""
    
    def __init__(self):
        self._mouse = None
        self._keyboard = None
        self._initialized = False
    
    def initialize(self):
        """Initialize input handlers."""
        try:
            from pynput.mouse import Controller as MouseController
            from pynput.keyboard import Controller as KeyboardController
            
            self._mouse = MouseController()
            self._keyboard = KeyboardController()
            self._initialized = True
            logger.info("Input handlers initialized")
        except ImportError:
            logger.error("pynput not available")
            self._initialized = False
    
    def click(self, x: int = None, y: int = None):
        """Click at position."""
        if not self._initialized or not self._mouse:
            return
        
        if x is not None and y is not None:
            self._mouse.position = (x, y)
        
        self._mouse.click()
    
    def press(self, key: str):
        """Press key."""
        if not self._initialized or not self._keyboard:
            return
        
        self._keyboard.press(key)
    
    def release(self, key: str):
        """Release key."""
        if not self._initialized or not self._keyboard:
            return
        
        self._keyboard.release(key)
