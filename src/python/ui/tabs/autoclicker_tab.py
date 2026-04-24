"""Autoclicker Tab UI Component"""

import logging
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QDoubleSpinBox,
    QCheckBox, QPushButton, QComboBox, QGroupBox, QSlider
)
from PyQt6.QtCore import Qt, pyqtSignal, QThread
from PyQt6.QtGui import QFont

from core.autoclicker import Autoclicker

logger = logging.getLogger(__name__)


class AutoclickerTab(QWidget):
    """Autoclicker configuration and control tab."""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.autoclicker = Autoclicker()
        self.is_running = False
        
        self._init_ui()
        logger.info("AutoclickerTab initialized")
    
    def _init_ui(self):
        """Initialize UI components."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Autoclicker")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # CPS Control Group
        cps_group = QGroupBox("CPS Control")
        cps_layout = QHBoxLayout()
        
        cps_layout.addWidget(QLabel("CPS:"))
        self.cps_spin = QSpinBox()
        self.cps_spin.setMinimum(1)
        self.cps_spin.setMaximum(20)
        self.cps_spin.setValue(8)
        cps_layout.addWidget(self.cps_spin)
        
        cps_layout.addWidget(QLabel("Jitter:"))
        self.jitter_spin = QDoubleSpinBox()
        self.jitter_spin.setMinimum(0.0)
        self.jitter_spin.setMaximum(1.0)
        self.jitter_spin.setValue(0.1)
        self.jitter_spin.setSingleStep(0.05)
        cps_layout.addWidget(self.jitter_spin)
        
        cps_group.setLayout(cps_layout)
        layout.addWidget(cps_group)
        
        # Mode Selection
        mode_group = QGroupBox("Click Mode")
        mode_layout = QHBoxLayout()
        
        mode_layout.addWidget(QLabel("Mode:"))
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Click", "Hold", "Toggle"])
        mode_layout.addWidget(self.mode_combo)
        
        mode_group.setLayout(mode_layout)
        layout.addWidget(mode_group)
        
        # Button Control Group
        button_group = QGroupBox("Control")
        button_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self._on_start)
        button_layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self._on_stop)
        self.stop_btn.setEnabled(False)
        button_layout.addWidget(self.stop_btn)
        
        button_group.setLayout(button_layout)
        layout.addWidget(button_group)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def _on_start(self):
        """Start autoclicker."""
        try:
            cps = self.cps_spin.value()
            jitter = self.jitter_spin.value()
            mode = self.mode_combo.currentText().lower()
            
            self.autoclicker.start(cps=cps, jitter=jitter, mode=mode)
            self.is_running = True
            
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            
            logger.info(f"Autoclicker started: CPS={cps}, jitter={jitter}, mode={mode}")
        except Exception as e:
            logger.error(f"Failed to start autoclicker: {e}")
    
    def _on_stop(self):
        """Stop autoclicker."""
        try:
            self.autoclicker.stop()
            self.is_running = False
            
            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            
            logger.info("Autoclicker stopped")
        except Exception as e:
            logger.error(f"Failed to stop autoclicker: {e}")
    
    def closeEvent(self, event):
        """Cleanup on close."""
        if self.is_running:
            self.autoclicker.stop()
        event.accept()
