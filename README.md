# 🎮 Hypixel SkyBlock Utility

A production-ready desktop application for Minecraft (Hypixel SkyBlock) with a modular hybrid architecture combining **C++ (performance-critical)** and **Python (rapid development)**.

## 📋 Features

- **Autoclicker** - High-precision CPS control with jitter and multiple modes
- **Advanced Macro System** - Record/playback with frame-perfect timing
- **Overlay System** - Always-on-top transparent windows with hotkey toggles
- **Bazaar Market Analyzer** - Real-time price tracking and flip suggestions
- **Wiki Viewer** - Fast searchable interface with cached content
- **Settings Management** - Comprehensive configuration with hotkey bindings

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────┐
│        Python Layer (PyQt6 UI)          │
│  ┌───────────────────────────────────┐  │
│  │ Main Window                       │  │
│  │ ├─ Autoclicker Tab                │  │
│  │ ├─ Macro Tab                      │  │
│  │ ├─ Bazaar Tab                     │  │
│  │ ├─ Wiki Tab                       │  │
│  │ └─ Settings Tab                   │  │
│  └───────────────────────────────────┘  │
├─────────────────────────────────────────┤
│        Core Services (Python)            │
│  ├─ Hotkey Manager                      │
│  ├─ Macro Engine                        │
│  ├─ API Handler (Bazaar/Wiki)           │
│  ├─ Settings Manager                    │
│  └─ Plugin System                       │
├─────────────────────────────────────────┤
│     C++ Layer (pybind11 bindings)       │
│  ├─ Input Engine (SendInput hooks)      │
│  ├─ Overlay Renderer (Win32/DirectX)    │
│  └─ Performance-Critical Timers         │
└─────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Visual Studio 2019+ (for C++ components)
- CMake 3.16+

### Installation

```bash
# Clone repository
git clone https://github.com/khouneeshraut/hypixel-skyblock-utility.git
cd hypixel-skyblock-utility

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Build C++ components
mkdir build && cd build
cmake ..
cmake --build . --config Release
cd ..

# Run application
python src/python/main.py
```

## 📦 Project Structure

```
hypixel-skyblock-utility/
├── src/
│   ├── python/
│   │   ├── main.py                    # Entry point
│   │   ├── ui/                        # PyQt6 UI components
│   │   │   ├── main_window.py
│   │   │   ├── tabs/
│   │   │   │   ├── autoclicker_tab.py
│   │   │   │   ├── macro_tab.py
│   │   │   │   ├── bazaar_tab.py
│   │   │   │   ├── wiki_tab.py
│   │   │   │   └── settings_tab.py
│   │   │   └── styles/
│   │   │       └── stylesheet.qss
│   │   ├── core/
│   │   │   ├── autoclicker.py         # Autoclicker implementation
│   │   │   ├── macro_engine.py        # Macro recording/playback
│   │   │   ├── hotkey_manager.py      # Global hotkey handling
│   │   │   └── input_handler.py       # Input abstractions
│   │   ├── services/
│   │   │   ├── bazaar_api.py          # Hypixel API integration
│   │   │   ├── wiki_service.py        # Wiki content management
│   │   │   ├── settings_manager.py    # Configuration persistence
│   │   │   └── cache_manager.py       # Caching layer
│   │   ├── models/
│   │   │   ├── macro.py
│   │   │   ├── bazaar_item.py
│   │   │   └── settings.py
│   │   └── utils/
│   │       ├── logging.py
│   │       ├── config.py
│   │       └── constants.py
│   └── cpp/
│       ├── input_engine.cpp
│       ├── input_engine.h
│       ├── overlay_renderer.cpp
│       ├── overlay_renderer.h
│       ├── high_precision_timer.h
│       ├── bindings.cpp
│       └── CMakeLists.txt
├── tests/
│   ├── unit/
│   │   ├── test_autoclicker.py
│   │   ├── test_macro_engine.py
│   │   ├── test_bazaar_api.py
│   │   └── test_settings_manager.py
│   ├── integration/
│   │   └── test_full_workflow.py
│   └── conftest.py
├── config/
│   ├── default_config.json
│   ├── hotkeys.json
│   └── bazaar_filters.json
├── requirements.txt
├── setup.py
├── CMakeLists.txt
├── .gitignore
└── docs/
    ├── ARCHITECTURE.md
    ├── DEVELOPMENT.md
    └── API.md
```

## 🔧 Key Dependencies

### Python
- **PyQt6** - Modern UI framework
- **pynput** - Global input/hotkey support
- **requests** - HTTP client
- **pandas** - Data analysis
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **spdlog** - Structured logging

### C++
- **pybind11** - Python bindings
- **cpr** - HTTP client
- **nlohmann/json** - JSON library
- **spdlog** - Logging

## 📚 Documentation

- [Architecture Details](docs/ARCHITECTURE.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [API Reference](docs/API.md)

## 🔐 Safety & Stability

- ✅ Thread-safe operations
- ✅ Macro execution timeouts
- ✅ Window focus detection
- ✅ Input validation
- ✅ Graceful shutdown handlers
- ✅ Rate limiting

## 📜 License

MIT

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

**Built with ❤️ for the SkyBlock community**
