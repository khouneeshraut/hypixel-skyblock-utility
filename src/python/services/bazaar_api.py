"""Hypixel Bazaar API Integration"""

import logging
import requests
from typing import List, Dict, Any
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class BazaarAPI:
    """Interface for Hypixel Bazaar API."""
    
    BASE_URL = "https://api.hypixel.net/skyblock/bazaar"
    CACHE_DURATION = 30  # seconds
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self._cache: Dict[str, Any] = {}
        self._cache_time: Dict[str, datetime] = {}
    
    def get_products(self) -> List[Dict[str, Any]]:
        """Fetch all bazaar products.
        
        Returns:
            List of product data dictionaries
        """
        try:
            cache_key = "bazaar_products"
            
            # Check cache
            if self._is_cache_valid(cache_key):
                logger.info("Using cached bazaar data")
                return self._cache[cache_key]
            
            response = requests.get(self.BASE_URL, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            products = []
            
            if "products" in data:
                for product_id, product_data in data["products"].items():
                    products.append({
                        "id": product_id,
                        "name": product_data.get("product_name", product_id),
                        "buy_price": product_data.get("quick_status", {}).get("buyPrice"),
                        "sell_price": product_data.get("quick_status", {}).get("sellPrice"),
                        "buy_volume": product_data.get("quick_status", {}).get("buyVolume"),
                        "sell_volume": product_data.get("quick_status", {}).get("sellVolume"),
                    })
            
            # Cache results
            self._cache[cache_key] = products
            self._cache_time[cache_key] = datetime.now()
            
            logger.info(f"Fetched {len(products)} bazaar products")
            return products
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch bazaar data: {e}")
            return []
    
    def get_product(self, product_id: str) -> Dict[str, Any]:
        """Get specific product data.
        
        Args:
            product_id: Product ID (e.g., 'WHEAT')
        
        Returns:
            Product data dictionary
        """
        try:
            response = requests.get(f"{self.BASE_URL}", params={"item": product_id}, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if "products" in data and product_id in data["products"]:
                return data["products"][product_id]
            
            return {}
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch product {product_id}: {e}")
            return {}
    
    def calculate_flip_profit(self, product_id: str) -> float:
        """Calculate potential flip profit.
        
        Args:
            product_id: Product ID
        
        Returns:
            Profit percentage
        """
        try:
            product = self.get_product(product_id)
            
            quick_status = product.get("quick_status", {})
            buy_price = quick_status.get("buyPrice")
            sell_price = quick_status.get("sellPrice")
            
            if not buy_price or not sell_price:
                return 0.0
            
            profit = ((sell_price - buy_price) / buy_price) * 100
            return profit
        
        except Exception as e:
            logger.error(f"Failed to calculate flip profit: {e}")
            return 0.0
    
    def _is_cache_valid(self, key: str) -> bool:
        """Check if cache entry is still valid."""
        if key not in self._cache_time:
            return False
        
        age = datetime.now() - self._cache_time[key]
        return age < timedelta(seconds=self.CACHE_DURATION)
