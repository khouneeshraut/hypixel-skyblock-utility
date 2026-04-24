"""Wiki Viewer Tab UI Component"""

import logging
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QTextEdit, QListWidget, QListWidgetItem, QSplitter
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from services.wiki_service import WikiService

logger = logging.getLogger(__name__)


class WikiTab(QWidget):
    """Wiki viewer and search tab."""
    
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.wiki_service = WikiService()
        
        self._init_ui()
        logger.info("WikiTab initialized")
    
    def _init_ui(self):
        """Initialize UI components."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Wiki Viewer")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # Search bar
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search:"))
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search wiki...")
        self.search_input.textChanged.connect(self._on_search)
        search_layout.addWidget(self.search_input)
        
        layout.addLayout(search_layout)
        
        # Content area with splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Search results list
        self.results_list = QListWidget()
        self.results_list.itemClicked.connect(self._on_result_selected)
        splitter.addWidget(self.results_list)
        
        # Content display
        self.content_display = QTextEdit()
        self.content_display.setReadOnly(True)
        splitter.addWidget(self.content_display)
        
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        
        layout.addWidget(splitter)
        self.setLayout(layout)
    
    def _on_search(self, query):
        """Handle search input."""
        if not query or len(query) < 2:
            self.results_list.clear()
            return
        
        try:
            results = self.wiki_service.search(query)
            self.results_list.clear()
            
            for result in results:
                item = QListWidgetItem(result['title'])
                item.setData(Qt.ItemDataRole.UserRole, result['url'])
                self.results_list.addItem(item)
            
            logger.info(f"Found {len(results)} wiki results for '{query}'")
        except Exception as e:
            logger.error(f"Wiki search failed: {e}")
    
    def _on_result_selected(self, item):
        """Handle result selection."""
        try:
            url = item.data(Qt.ItemDataRole.UserRole)
            content = self.wiki_service.get_content(url)
            self.content_display.setText(content)
            logger.info(f"Loaded wiki content from {url}")
        except Exception as e:
            logger.error(f"Failed to load wiki content: {e}")
