#!/usr/bin/env python3
"""
Hypixel SkyBlock Utility - Main Entry Point

A production-ready desktop application combining C++ and Python
for high-performance Minecraft utility features.
"""

import sys
import logging
from pathlib import Path

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from ui.main_window import MainWindow
from utils.config import load_config


def main():
    """Application entry point."""
    try:
        logger.info("Starting Hypixel SkyBlock Utility...")
        
        # Load configuration
        config = load_config()
        logger.info(f"Loaded configuration: {config}")
        
        # Create application
        app = QApplication(sys.argv)
        app.setApplicationName("Hypixel SkyBlock Utility")
        app.setApplicationVersion("0.1.0")
        
        # Set application style
        app.setStyle('Fusion')
        
        # Create and show main window
        window = MainWindow(config)
        window.show()
        
        logger.info("Application started successfully")
        sys.exit(app.exec())
        
    except Exception as e:
        logger.exception(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
