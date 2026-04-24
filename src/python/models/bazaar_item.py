"""Bazaar Item Data Model"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class BazaarItem:
    """Bazaar product item."""
    product_id: str
    product_name: str
    buy_price: float
    sell_price: float
    buy_volume: int
    sell_volume: int
    profit_margin: float = 0.0
    profit_percentage: float = 0.0
    
    def calculate_profit(self) -> float:
        """Calculate profit margin."""
        self.profit_margin = self.sell_price - self.buy_price
        if self.buy_price > 0:
            self.profit_percentage = (self.profit_margin / self.buy_price) * 100
        return self.profit_margin
