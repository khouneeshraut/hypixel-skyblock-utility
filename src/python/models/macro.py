"""Macro Data Model"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class MacroEvent:
    """Single event in a macro."""
    event_type: str
    timestamp: float
    key: Optional[str] = None
    button: Optional[str] = None
    x: Optional[int] = None
    y: Optional[int] = None
    relative_time: float = 0.0


@dataclass
class Macro:
    """Complete macro recording."""
    name: str
    events: List[MacroEvent] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    duration: float = 0.0
    category: str = "default"
    description: str = ""
