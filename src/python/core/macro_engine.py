"""Macro Recording and Playback Engine"""

import logging
import threading
import time
from typing import List, Optional
from dataclasses import dataclass, field
from datetime import datetime

try:
    from pynput.mouse import Button, Controller as MouseController, Listener as MouseListener
    from pynput.keyboard import Controller as KeyboardController, Listener as KeyboardListener
except ImportError:
    MouseController = None
    KeyboardController = None

logger = logging.getLogger(__name__)


@dataclass
class MacroEvent:
    """Single macro event."""
    event_type: str  # 'key_press', 'key_release', 'mouse_click', 'mouse_move'
    timestamp: float
    key: Optional[str] = None
    button: Optional[str] = None
    x: Optional[int] = None
    y: Optional[int] = None
    relative_time: float = field(default=0.0)  # Time since last event


class MacroEngine:
    """Record and playback macros with frame-perfect timing."""
    
    def __init__(self):
        self.mouse = MouseController() if MouseController else None
        self.keyboard = KeyboardController() if KeyboardController else None
        
        self._recording = False
        self._playing = False
        self._events: List[MacroEvent] = []
        self._start_time: float = 0.0
        self._mouse_listener: Optional[MouseListener] = None
        self._keyboard_listener: Optional[KeyboardListener] = None
    
    def start_recording(self):
        """Start recording macro events."""
        if self._recording:
            logger.warning("Already recording")
            return
        
        self._events = []
        self._start_time = time.time()
        self._recording = True
        
        # Setup listeners
        self._mouse_listener = MouseListener(on_click=self._on_mouse_click)
        self._keyboard_listener = KeyboardListener(on_press=self._on_key_press, on_release=self._on_key_release)
        
        self._mouse_listener.start()
        self._keyboard_listener.start()
        
        logger.info("Macro recording started")
    
    def stop_recording(self):
        """Stop recording and save events."""
        if not self._recording:
            return
        
        self._recording = False
        
        if self._mouse_listener:
            self._mouse_listener.stop()
        if self._keyboard_listener:
            self._keyboard_listener.stop()
        
        # Calculate relative times
        if self._events:
            for i, event in enumerate(self._events):
                if i == 0:
                    event.relative_time = 0.0
                else:
                    event.relative_time = event.timestamp - self._events[i-1].timestamp
        
        logger.info(f"Macro recording stopped: {len(self._events)} events recorded")
    
    def play(self, speed_multiplier: float = 1.0, loops: int = 1):
        """Play recorded macro.
        
        Args:
            speed_multiplier: Speed multiplier (0.5-2.0)
            loops: Number of times to repeat (1-100)
        """
        if not self._events:
            logger.warning("No macro recorded to play")
            return
        
        if self._playing:
            logger.warning("Already playing")
            return
        
        self._playing = True
        thread = threading.Thread(
            target=self._playback_loop,
            args=(speed_multiplier, loops),
            daemon=True
        )
        thread.start()
        logger.info(f"Macro playback started: speed={speed_multiplier}, loops={loops}")
    
    def stop_playback(self):
        """Stop macro playback."""
        self._playing = False
        logger.info("Macro playback stopped")
    
    def _playback_loop(self, speed_multiplier: float, loops: int):
        """Main playback loop."""
        try:
            for loop_num in range(loops):
                if not self._playing:
                    break
                
                for event in self._events:
                    if not self._playing:
                        break
                    
                    # Wait for relative time
                    delay = event.relative_time / speed_multiplier
                    time.sleep(delay)
                    
                    # Execute event
                    self._execute_event(event)
                
                logger.info(f"Macro loop {loop_num + 1}/{loops} completed")
        except Exception as e:
            logger.error(f"Error during macro playback: {e}")
        finally:
            self._playing = False
    
    def _execute_event(self, event: MacroEvent):
        """Execute a single macro event."""
        try:
            if event.event_type == "mouse_click" and self.mouse:
                button = Button.left if event.button == "left" else Button.right
                self.mouse.click(button, 1)
            elif event.event_type == "mouse_move" and self.mouse:
                self.mouse.position = (event.x, event.y)
            elif event.event_type == "key_press" and self.keyboard:
                self.keyboard.press(event.key)
            elif event.event_type == "key_release" and self.keyboard:
                self.keyboard.release(event.key)
        except Exception as e:
            logger.error(f"Error executing event: {e}")
    
    def _on_mouse_click(self, x, y, button, pressed):
        """Handle mouse click event."""
        if not self._recording:
            return
        
        event = MacroEvent(
            event_type="mouse_click",
            timestamp=time.time() - self._start_time,
            button=str(button).split('.')[-1].lower(),
            x=x,
            y=y
        )
        self._events.append(event)
    
    def _on_key_press(self, key):
        """Handle key press event."""
        if not self._recording:
            return
        
        event = MacroEvent(
            event_type="key_press",
            timestamp=time.time() - self._start_time,
            key=str(key)
        )
        self._events.append(event)
    
    def _on_key_release(self, key):
        """Handle key release event."""
        if not self._recording:
            return
        
        event = MacroEvent(
            event_type="key_release",
            timestamp=time.time() - self._start_time,
            key=str(key)
        )
        self._events.append(event)
