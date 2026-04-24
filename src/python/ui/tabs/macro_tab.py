"""Macro System Tab UI Component"""

import logging
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget,
    QListWidgetItem, QGroupBox, QSpinBox, QDoubleSpinBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from core.macro_engine import MacroEngine

logger = logging.getLogger(__name__)


class MacroTab(QWidget):
    """Macro recording and playback tab."""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.macro_engine = MacroEngine()
        self.is_recording = False
        self.is_playing = False
        
        self._init_ui()
        logger.info("MacroTab initialized")
    
    def _init_ui(self):
        """Initialize UI components."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Macro System")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Recording Group
        record_group = QGroupBox("Recording")
        record_layout = QVBoxLayout()
        
        button_layout = QHBoxLayout()
        
        self.record_btn = QPushButton("Record")
        self.record_btn.clicked.connect(self._on_record)
        button_layout.addWidget(self.record_btn)
        
        self.stop_record_btn = QPushButton("Stop Recording")
        self.stop_record_btn.clicked.connect(self._on_stop_record)
        self.stop_record_btn.setEnabled(False)
        button_layout.addWidget(self.stop_record_btn)
        
        record_layout.addLayout(button_layout)
        record_group.setLayout(record_layout)
        layout.addWidget(record_group)
        
        # Playback Group
        playback_group = QGroupBox("Playback")
        playback_layout = QVBoxLayout()
        
        # Speed control
        speed_h_layout = QHBoxLayout()
        speed_h_layout.addWidget(QLabel("Speed Multiplier:"))
        self.speed_spin = QDoubleSpinBox()
        self.speed_spin.setMinimum(0.5)
        self.speed_spin.setMaximum(2.0)
        self.speed_spin.setValue(1.0)
        self.speed_spin.setSingleStep(0.1)
        speed_h_layout.addWidget(self.speed_spin)
        speed_h_layout.addStretch()
        playback_layout.addLayout(speed_h_layout)
        
        # Loop control
        loop_h_layout = QHBoxLayout()
        loop_h_layout.addWidget(QLabel("Loops:"))
        self.loops_spin = QSpinBox()
        self.loops_spin.setMinimum(1)
        self.loops_spin.setMaximum(100)
        self.loops_spin.setValue(1)
        loop_h_layout.addWidget(self.loops_spin)
        loop_h_layout.addStretch()
        playback_layout.addLayout(loop_h_layout)
        
        # Playback buttons
        play_button_layout = QHBoxLayout()
        
        self.play_btn = QPushButton("Play")
        self.play_btn.clicked.connect(self._on_play)
        play_button_layout.addWidget(self.play_btn)
        
        self.stop_play_btn = QPushButton("Stop")
        self.stop_play_btn.clicked.connect(self._on_stop_play)
        self.stop_play_btn.setEnabled(False)
        play_button_layout.addWidget(self.stop_play_btn)
        
        playback_layout.addLayout(play_button_layout)
        playback_group.setLayout(playback_layout)
        layout.addWidget(playback_group)
        
        # Macro list
        layout.addWidget(QLabel("Saved Macros:"))
        self.macro_list = QListWidget()
        layout.addWidget(self.macro_list)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def _on_record(self):
        """Start recording macro."""
        try:
            self.macro_engine.start_recording()
            self.is_recording = True
            self.record_btn.setEnabled(False)
            self.stop_record_btn.setEnabled(True)
            logger.info("Macro recording started")
        except Exception as e:
            logger.error(f"Failed to start recording: {e}")
    
    def _on_stop_record(self):
        """Stop recording macro."""
        try:
            self.macro_engine.stop_recording()
            self.is_recording = False
            self.record_btn.setEnabled(True)
            self.stop_record_btn.setEnabled(False)
            logger.info("Macro recording stopped")
        except Exception as e:
            logger.error(f"Failed to stop recording: {e}")
    
    def _on_play(self):
        """Play macro."""
        try:
            speed = self.speed_spin.value()
            loops = self.loops_spin.value()
            
            self.macro_engine.play(speed_multiplier=speed, loops=loops)
            self.is_playing = True
            self.play_btn.setEnabled(False)
            self.stop_play_btn.setEnabled(True)
            logger.info(f"Macro playback started: speed={speed}, loops={loops}")
        except Exception as e:
            logger.error(f"Failed to play macro: {e}")
    
    def _on_stop_play(self):
        """Stop macro playback."""
        try:
            self.macro_engine.stop_playback()
            self.is_playing = False
            self.play_btn.setEnabled(True)
            self.stop_play_btn.setEnabled(False)
            logger.info("Macro playback stopped")
        except Exception as e:
            logger.error(f"Failed to stop playback: {e}")
