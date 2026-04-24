"""Settings Tab UI Component"""

import logging
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget,
    QGroupBox, QLineEdit, QSpinBox, QCheckBox
)
from PyQt6.QtGui import QFont

from services.settings_manager import SettingsManager

logger = logging.getLogger(__name__)


class SettingsTab(QWidget):
    """Application settings tab."""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.settings_manager = SettingsManager()
        
        self._init_ui()
        logger.info("SettingsTab initialized")
    
    def _init_ui(self):
        """Initialize UI components."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Settings")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Settings tabs
        settings_tabs = QTabWidget()
        
        # General settings
        general_group = QGroupBox("General")
        general_layout = QVBoxLayout()
        
        general_layout.addWidget(QLabel("Theme:"))
        general_layout.addWidget(QLineEdit("Dark"))
        
        general_layout.addWidget(QCheckBox("Run on startup"))
        general_layout.addWidget(QCheckBox("Auto-update"))
        
        general_group.setLayout(general_layout)
        settings_tabs.addTab(general_group, "General")
        
        # Hotkey settings
        hotkey_group = QGroupBox("Hotkeys")
        hotkey_layout = QVBoxLayout()
        
        hotkey_items = [
            ("Toggle Window", "Alt+Shift+H"),
            ("Start Autoclicker", "Alt+A"),
            ("Start Macro", "Alt+M"),
        ]
        
        for name, hotkey in hotkey_items:
            h_layout = QHBoxLayout()
            h_layout.addWidget(QLabel(name))
            h_layout.addWidget(QLineEdit(hotkey))
            hotkey_layout.addLayout(h_layout)
        
        hotkey_group.setLayout(hotkey_layout)
        settings_tabs.addTab(hotkey_group, "Hotkeys")
        
        # API settings
        api_group = QGroupBox("API")
        api_layout = QVBoxLayout()
        
        api_layout.addWidget(QLabel("Cache Duration (minutes):"))
        cache_spin = QSpinBox()
        cache_spin.setValue(30)
        api_layout.addWidget(cache_spin)
        
        api_layout.addWidget(QCheckBox("Enable caching"))
        
        api_group.setLayout(api_layout)
        settings_tabs.addTab(api_group, "API")
        
        layout.addWidget(settings_tabs)
        
        # Save/Reset buttons
        button_layout = QHBoxLayout()
        
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self._on_save)
        button_layout.addWidget(save_btn)
        
        reset_btn = QPushButton("Reset to Default")
        reset_btn.clicked.connect(self._on_reset)
        button_layout.addWidget(reset_btn)
        
        button_layout.addStretch()
        layout.addLayout(button_layout)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def _on_save(self):
        """Save settings."""
        try:
            # Settings save logic here
            logger.info("Settings saved")
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
    
    def _on_reset(self):
        """Reset settings to default."""
        try:
            self.settings_manager.reset_to_default()
            logger.info("Settings reset to default")
        except Exception as e:
            logger.error(f"Failed to reset settings: {e}")
