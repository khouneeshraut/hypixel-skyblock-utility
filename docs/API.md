# API Reference

## Core Classes

### Autoclicker

```python
from src.python.core.autoclicker import Autoclicker

clicker = Autoclicker()

# Start clicking
clicker.start(
    cps=8,           # Clicks per second (1-20)
    jitter=0.1,      # Random delay variance (0.0-1.0)
    mode="click"     # Mode: "click", "hold", or "toggle"
)

# Stop clicking
clicker.stop()
```

### MacroEngine

```python
from src.python.core.macro_engine import MacroEngine

engine = MacroEngine()

# Record macro
engine.start_recording()
# ... perform actions ...
engine.stop_recording()

# Playback macro
engine.play(
    speed_multiplier=1.0,  # Speed multiplier (0.5-2.0)
    loops=1                # Number of repetitions (1-100)
)

# Stop playback
engine.stop_playback()
```

### HotkeyManager

```python
from src.python.core.hotkey_manager import HotkeyManager

manager = HotkeyManager()

# Register hotkey
def on_hotkey():
    print("Hotkey pressed!")

manager.register("<alt>+<shift>+h", on_hotkey)

# Unregister hotkey
manager.unregister("<alt>+<shift>+h")

# Cleanup
manager.cleanup()
```

## Services

### BazaarAPI

```python
from src.python.services.bazaar_api import BazaarAPI

api = BazaarAPI(api_key="your_key_here")

# Get all products
products = api.get_products()
for product in products:
    print(f"{product['name']}: {product['buy_price']}")

# Get specific product
wheat = api.get_product("WHEAT")

# Calculate flip profit
profit = api.calculate_flip_profit("WHEAT")
print(f"Profit: {profit}%")
```

### WikiService

```python
from src.python.services.wiki_service import WikiService

wiki = WikiService()

# Search wiki
results = wiki.search("farming")
for result in results:
    print(f"{result['title']}: {result['url']}")

# Get page content
content = wiki.get_content("https://hypixel.fandom.com/wiki/Farming")
print(content)
```

### SettingsManager

```python
from src.python.services.settings_manager import SettingsManager
from pathlib import Path

manager = SettingsManager(config_dir=Path.home() / ".config/app")

# Get setting
theme = manager.get("theme", "dark")

# Set setting
manager.set("theme", "light")

# Reset to defaults
manager.reset_to_default()
```

## Models

### MacroEvent

```python
from src.python.core.macro_engine import MacroEvent

event = MacroEvent(
    event_type="key_press",      # Event type
    timestamp=1.234,             # Time since recording start
    key="a",                     # Key pressed
    relative_time=0.05           # Time since last event
)
```

### Macro

```python
from src.python.models.macro import Macro, MacroEvent

macro = Macro(
    name="Farm Macro",
    category="farming",
    description="Automated farming sequence",
    events=[...]  # List of MacroEvent
)

# Properties
print(f"Duration: {macro.duration}s")
print(f"Events: {len(macro.events)}")
```

### BazaarItem

```python
from src.python.models.bazaar_item import BazaarItem

item = BazaarItem(
    product_id="WHEAT",
    product_name="Wheat",
    buy_price=1.0,
    sell_price=1.5,
    buy_volume=10000,
    sell_volume=5000
)

profit = item.calculate_profit()
print(f"Profit margin: {item.profit_margin}")
print(f"Profit %: {item.profit_percentage}%")
```

## C++ Bindings

### InputEngine (C++)

```python
from hypixel_core import InputEngine

engine = InputEngine()

# Click at position
engine.click(x=100, y=200, button=0)  # button: 0=left, 1=right, 2=middle

# Move mouse
engine.move(x=500, y=300)

# Keyboard input
engine.press_key(65)   # VK_A
engine.release_key(65)

# Get mouse position
x, y = engine.get_mouse_position()

# Check window focus
if engine.window_in_focus():
    print("Minecraft window is focused")
```

### OverlayRenderer (C++)

```python
from hypixel_core import OverlayRenderer

renderer = OverlayRenderer()

# Initialize
if renderer.initialize():
    # Show overlay
    renderer.show()
    
    # Draw text
    renderer.draw_text("Status: Running", 10.0, 10.0)
    
    # Present frame
    renderer.present()
    
    # Toggle visibility
    renderer.toggle()
    
    # Hide overlay
    renderer.hide()
```

### HighPrecisionTimer (C++)

```python
from hypixel_core import HighPrecisionTimer

timer = HighPrecisionTimer()
timer.start()

# ... do work ...

elapsed = timer.elapsed_ms()
print(f"Elapsed: {elapsed}ms")

# Precise sleep
HighPrecisionTimer.precise_sleep(10.5)  # Sleep 10.5ms
```

## Configuration Files

### default_config.json

```json
{
  "app_name": "Hypixel SkyBlock Utility",
  "version": "0.1.0",
  "theme": "dark",
  "autostart": false,
  "api": {
    "cache_duration": 30,
    "timeout": 10,
    "retry_count": 3
  },
  "autoclicker": {
    "default_cps": 8,
    "max_cps": 20,
    "default_jitter": 0.1
  }
}
```

### hotkeys.json

```json
{
  "hotkeys": {
    "toggle_window": "<alt>+<shift>+h",
    "autoclicker_start": "<alt>+a",
    "autoclicker_stop": "<alt>+s",
    "macro_start": "<alt>+m",
    "macro_stop": "<alt>+n",
    "emergency_stop": "<esc>"
  }
}
```

## Exception Handling

### Common Exceptions

```python
try:
    clicker.start(cps=25)  # Invalid CPS
except ValueError as e:
    print(f"Invalid parameter: {e}")

try:
    api.get_products()
except requests.exceptions.RequestException as e:
    print(f"API error: {e}")

try:
    manager.set("key", "value")
except IOError as e:
    print(f"Settings save failed: {e}")
```

## Logging

```python
import logging

# Get logger
logger = logging.getLogger(__name__)

# Log levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

---

**For more details on architecture, see ARCHITECTURE.md**
