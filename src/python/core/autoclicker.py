"""Autoclicker Implementation"""

import logging
import threading
import time
import random
from typing import Optional

try:
    from pynput.mouse import Button, Controller as MouseController
except ImportError:
    Button = None
    MouseController = None

logger = logging.getLogger(__name__)


class Autoclicker:
    """High-performance autoclicker with multiple modes."""
    
    MODES = {"click", "hold", "toggle"}
    
    def __init__(self):
        self.mouse = MouseController() if MouseController else None
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._mode = "click"
        self._cps = 8
        self._jitter = 0.0
        self._hold_down = False
    
    def start(self, cps: int = 8, jitter: float = 0.0, mode: str = "click"):
        """Start autoclicker.
        
        Args:
            cps: Clicks per second (1-20)
            jitter: Random delay variance (0.0-1.0)
            mode: Click mode - 'click', 'hold', or 'toggle'
        """
        if self._running:
            logger.warning("Autoclicker already running")
            return
        
        if mode not in self.MODES:
            raise ValueError(f"Invalid mode: {mode}. Must be one of {self.MODES}")
        
        if not (1 <= cps <= 20):
            raise ValueError(f"CPS must be between 1 and 20, got {cps}")
        
        if not (0.0 <= jitter <= 1.0):
            raise ValueError(f"Jitter must be between 0.0 and 1.0, got {jitter}")
        
        self._cps = cps
        self._jitter = jitter
        self._mode = mode
        self._running = True
        
        self._thread = threading.Thread(target=self._click_loop, daemon=True)
        self._thread.start()
        
        logger.info(f"Autoclicker started: CPS={cps}, jitter={jitter}, mode={mode}")
    
    def stop(self):
        """Stop autoclicker."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)
        logger.info("Autoclicker stopped")
    
    def _click_loop(self):
        """Main clicking loop."""
        interval = 1.0 / self._cps
        
        while self._running:
            try:
                if self._mode == "click":
                    self._perform_click()
                elif self._mode == "hold":
                    self._perform_hold()
                elif self._mode == "toggle":
                    self._perform_toggle()
                
                # Apply jitter
                delay = interval + random.uniform(-self._jitter, self._jitter)
                delay = max(delay, 0.001)  # Ensure positive delay
                
                time.sleep(delay)
            except Exception as e:
                logger.error(f"Error in click loop: {e}")
                break
    
    def _perform_click(self):
        """Perform single click."""
        if self.mouse:
            self.mouse.click(Button.left, 1)
    
    def _perform_hold(self):
        """Perform hold down."""
        if self.mouse:
            if not self._hold_down:
                self.mouse.press(Button.left)
                self._hold_down = True
    
    def _perform_toggle(self):
        """Toggle hold state."""
        if self.mouse:
            if self._hold_down:
                self.mouse.release(Button.left)
                self._hold_down = False
            else:
                self.mouse.press(Button.left)
                self._hold_down = True
    
    def __del__(self):
        """Cleanup on delete."""
        if self._running:
            self.stop()
