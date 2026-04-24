"""Main Application Window"""

import logging
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QStatusBar
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QIcon

from .tabs.autoclicker_tab import AutoclickerTab
from .tabs.macro_tab import MacroTab
from .tabs.bazaar_tab import BazaarTab
from .tabs.wiki_tab import WikiTab
from .tabs.settings_tab import SettingsTab
from core.hotkey_manager import HotkeyManager

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.hotkey_manager = HotkeyManager()
        
        self.setWindowTitle("Hypixel SkyBlock Utility")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialize UI
        self._init_ui()
        self._setup_hotkeys()
        
        logger.info("MainWindow initialized")
    
    def _init_ui(self):
        """Initialize user interface components."""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout(central_widget)
        
        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.addTab(AutoclickerTab(self.config), "Autoclicker")
        self.tabs.addTab(MacroTab(self.config), "Macro")
        self.tabs.addTab(BazaarTab(self.config), "Bazaar")
        self.tabs.addTab(WikiTab(self.config), "Wiki")
        self.tabs.addTab(SettingsTab(self.config), "Settings")
        
        layout.addWidget(self.tabs)
        central_widget.setLayout(layout)
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
    
    def _setup_hotkeys(self):
        """Setup global hotkeys."""
        # Register hotkey to toggle main window visibility
        try:
            self.hotkey_manager.register(
                'alt+shift+h',
                self._toggle_visibility
            )
            logger.info("Hotkeys registered successfully")
        except Exception as e:
            logger.error(f"Failed to register hotkeys: {e}")
    
    def _toggle_visibility(self):
        """Toggle main window visibility."""
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()
    
    def closeEvent(self, event):
        """Handle window close event."""
        self.hotkey_manager.cleanup()
        event.accept()
        logger.info("Application closed")
