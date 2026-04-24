# Architecture Documentation

## 🏗️ System Architecture

### Overview

The Hypixel SkyBlock Utility is built on a **hybrid C++/Python architecture** that combines:

- **Python Layer**: User interface, API integration, business logic
- **C++ Layer**: High-performance input handling, rendering, timing
- **IPC Communication**: pybind11 bindings for seamless integration

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Application (main.py)                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  PyQt6 Main Window                          │
│  ┌──────────┬─────────┬────────┬──────┬──────────┐         │
│  │Autoclicker│ Macro   │ Bazaar │ Wiki │ Settings │         │
│  └──────────┴─────────┴────────┴──────┴──────────┘         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                 Core Services (Python)                      │
│  ┌──────────┬──────────┬──────────┬────────┬─────────┐     │
│  │Hotkey    │Autoclicker│Macro   │Bazaar  │ Wiki    │     │
│  │Manager   │Service    │Engine  │API     │Service  │     │
│  └──────────┴──────────┴──────────┴────────┴─────────┘     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              C++ Performance Layer (pybind11)               │
│  ┌──────────┬────────────┬──────────────────┐              │
│  │Input     │ Overlay    │ High Precision   │              │
│  │Engine    │ Renderer   │ Timer            │              │
│  └──────────┴────────────┴──────────────────┘              │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                Windows API / DirectX                        │
│  ┌──────────┬──────────┬──────────┬───────────┐           │
│  │User32    │Kernel32  │DirectX11 │ DXGI      │           │
│  └──────────┴──────────┴──────────┴───────────┘           │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Module Breakdown

### Python Modules

#### UI Layer (`ui/`)

```
ui/
├── main_window.py      # Main application window
├── tabs/
│   ├── autoclicker_tab.py   # Autoclicker UI
│   ├── macro_tab.py         # Macro recording/playback
│   ├── bazaar_tab.py        # Market analyzer
│   ├── wiki_tab.py          # Wiki viewer
│   └── settings_tab.py      # Settings
└── styles/
    └── stylesheet.qss  # Qt stylesheets
```

**Responsibilities:**
- Render user interface
- Handle user input events
- Manage tab switching
- Display data and status updates

#### Core Engines (`core/`)

```
core/
├── autoclicker.py      # Autoclicker implementation
├── macro_engine.py     # Macro recording/playback
├── hotkey_manager.py   # Global hotkey handling
└── input_handler.py    # Input abstraction layer
```

**Key Classes:**

- **Autoclicker**: Threaded clicking with CPS control
- **MacroEngine**: Event recording and frame-perfect playback
- **HotkeyManager**: Global hotkey registration and handling
- **InputHandler**: Abstraction for pynput operations

#### Services (`services/`)

```
services/
├── bazaar_api.py       # Hypixel API integration
├── wiki_service.py     # Wiki content management
├── settings_manager.py # Configuration persistence
└── cache_manager.py    # Caching layer
```

**Features:**
- External API communication
- Data caching and rate limiting
- Configuration management
- Error handling and retry logic

#### Models (`models/`)

```
models/
├── macro.py           # Macro data structure
├── bazaar_item.py     # Market item model
└── settings.py        # Settings model
```

**Purpose:**
- Type-safe data representation
- Serialization/deserialization
- Data validation

#### Utilities (`utils/`)

```
utils/
├── config.py         # Configuration loading
├── logging.py        # Logging setup
└── constants.py      # Application constants
```

### C++ Modules

#### Input Engine (`input_engine.h/cpp`)

**Responsibilities:**
- Low-level mouse/keyboard input
- Windows API wrapper
- Window focus detection
- High-precision timing for clicks

**Key Methods:**
```cpp
void click(int x, int y, int button = 0);
void move(int x, int y);
void press_key(BYTE vk);
void release_key(BYTE vk);
bool window_in_focus();
```

#### Overlay Renderer (`overlay_renderer.h/cpp`)

**Responsibilities:**
- DirectX 11 overlay window
- Always-on-top rendering
- Text and graphics drawing
- Frame management

**Key Methods:**
```cpp
bool initialize();
void show();
void hide();
void toggle();
void draw_text(const std::string& text, float x, float y);
void present();
```

#### High Precision Timer (`high_precision_timer.h`)

**Responsibilities:**
- Sub-millisecond timing
- Frame-perfect macro playback
- Jitter control

## 🔄 Data Flow Examples

### Example 1: Autoclicker Workflow

```
1. User clicks "Start" in UI
   └→ AutoclickerTab._on_start()

2. Tab calls Autoclicker.start(cps=8, jitter=0.1)
   └→ Spawns worker thread

3. Worker thread runs _click_loop()
   └→ Calls _perform_click()

4. _perform_click() calls InputHandler.click()
   └→ Uses pynput for cross-platform support
   └→ OR calls C++ InputEngine for performance

5. InputEngine.click() calls Windows API
   └→ SendInput() executes the click

6. Loop continues with calculated delay
   └→ interval = 1.0 / CPS
   └→ Apply random jitter
   └→ Sleep and repeat
```

### Example 2: Macro Playback Workflow

```
1. User selects macro and clicks "Play"
   └→ MacroTab._on_play()

2. Tab calls MacroEngine.play(speed=1.0, loops=1)
   └→ Spawns playback thread

3. Playback thread iterates through recorded events
   └→ For each event:
      - Wait for relative_time / speed_multiplier
      - Call _execute_event()

4. _execute_event() uses InputHandler/C++ layer
   └→ Recreates original input
   └→ Maintains frame-perfect timing

5. After all events, loop counter incremented
   └→ Continue if loops > 0
   └→ Exit if loops exhausted
```

### Example 3: Bazaar API Workflow

```
1. User clicks "Refresh" in Bazaar tab
   └→ BazaarTab._on_refresh()

2. Tab calls BazaarAPI.get_products()
   └→ Check cache validity
   └→ If expired: fetch from Hypixel API
   └→ If valid: return cached data

3. API request with retry logic
   └→ Handle rate limiting
   └→ Timeout after 10 seconds
   └→ Retry up to 3 times on failure

4. Parse JSON response
   └→ Extract product data
   └→ Calculate profit margins
   └→ Store in cache (30 second TTL)

5. Return data to UI
   └→ Update market table
   └→ Display current prices and volumes
```

## 🔒 Thread Safety

### Thread-Safe Components

1. **Autoclicker**
   - `_running` flag (atomic)
   - Worker thread updates state
   - Main thread checks state

2. **Macro Engine**
   - `_events` list (locked during recording/playback)
   - Separate playback thread
   - Safe event access

3. **Settings Manager**
   - File-based locking (one instance)
   - JSON serialization
   - Atomic writes

### Synchronization Points

```python
# Autoclicker start/stop
_running = False  # Atomic flag
thread.join()     # Wait for thread

# Macro recording
listeners.start()     # Begin capturing
listeners.stop()      # End capturing
events.clear()        # Reset between recordings

# Settings updates
_lock = Lock()        # Protect file access
with _lock:
    _save_settings()
```

## 🔌 Integration Points

### Python ↔ C++

**pybind11 Module: `hypixel_core`**

```python
# Python side
from hypixel_core import InputEngine, OverlayRenderer

input_engine = InputEngine()
input_engine.click(100, 200)

renderer = OverlayRenderer()
renderer.initialize()
renderer.show()
```

**C++ Binding:**
```cpp
PYBIND11_MODULE(hypixel_core, m) {
    py::class_<InputEngine>(m, "InputEngine")
        .def("click", &InputEngine::click);
}
```

### External APIs

**Hypixel API**
- Endpoint: `https://api.hypixel.net/skyblock/bazaar`
- Rate Limit: 120 req/min
- Cache: 30 seconds (configurable)

**Wiki Service**
- Content Source: Hypixel Wiki
- Caching: In-memory + file-based
- Search: Fuzzy matching

## 📊 Performance Characteristics

### Autoclicker
- **CPS Range**: 1-20 clicks per second
- **Jitter**: 0-1.0 seconds variance
- **Accuracy**: ±1ms (with C++ layer)
- **CPU Usage**: <1% per CPS

### Macro System
- **Event Recording**: <1ms overhead
- **Playback Accuracy**: ±5ms (frame-perfect)
- **Memory**: ~100 bytes per event
- **Max Macro Size**: Limited by RAM

### Bazaar API
- **Cache Hit Rate**: ~90%
- **API Response**: ~500ms
- **Memory Footprint**: ~10MB (all products)
- **Update Frequency**: 30 seconds

## 🛡️ Error Handling

### Strategy: Graceful Degradation

1. **API Failures**
   - Use cached data if available
   - Retry with exponential backoff
   - User notification

2. **Input Failures**
   - Window focus loss → auto-stop
   - Timeout → emergency stop
   - Validation → skip invalid input

3. **Configuration Errors**
   - Load defaults on parse error
   - Validate on startup
   - User-friendly error messages

---

**For implementation details, see API.md**
