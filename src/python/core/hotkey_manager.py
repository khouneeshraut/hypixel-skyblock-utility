"""Global Hotkey Manager"""

import logging
from typing import Callable, Dict

try:
    from pynput.keyboard import GlobalHotKeys
except ImportError:
    GlobalHotKeys = None

logger = logging.getLogger(__name__)


class HotkeyManager:
    """Manage global hotkeys."""
    
    def __init__(self):
        self._hotkeys: Dict[str, Callable] = {}
        self._listener = None
        self._hotkey_objects = GlobalHotKeys({}) if GlobalHotKeys else None
    
    def register(self, hotkey: str, callback: Callable):
        """Register a global hotkey.
        
        Args:
            hotkey: Hotkey combination (e.g., '<alt>+<shift>+h')
            callback: Function to call when hotkey is pressed
        """
        if not GlobalHotKeys:
            logger.warning("pynput not available, hotkeys disabled")
            return
        
        self._hotkeys[hotkey] = callback
        
        try:
            if self._hotkey_objects:
                # Add to listener
                self._hotkey_objects = GlobalHotKeys(self._hotkeys)
                self._hotkey_objects.start()
            
            logger.info(f"Hotkey registered: {hotkey}")
        except Exception as e:
            logger.error(f"Failed to register hotkey {hotkey}: {e}")
    
    def unregister(self, hotkey: str):
        """Unregister a hotkey."""
        if hotkey in self._hotkeys:
            del self._hotkeys[hotkey]
            logger.info(f"Hotkey unregistered: {hotkey}")
    
    def cleanup(self):
        """Cleanup and stop listening."""
        if self._hotkey_objects:
            self._hotkey_objects.stop()
        self._hotkeys.clear()
        logger.info("Hotkey manager cleaned up")
