# Development and Testing Guide

## 🚀 Development Setup

### Environment Setup

```bash
# Clone repository
git clone https://github.com/khouneeshraut/hypixel-skyblock-utility.git
cd hypixel-skyblock-utility

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install -e .
```

### Building C++ Components

```bash
# Create build directory
mkdir build && cd build

# Configure with CMake
cmake ..

# Build (Windows)
cmake --build . --config Release

# Build (Linux/Mac)
make -j$(nproc)
```

## 🧪 Testing

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test Suite

```bash
pytest tests/unit/test_autoclicker.py -v
pytest tests/unit/test_macro_engine.py -v
pytest tests/unit/test_bazaar_api.py -v
```

### Run with Coverage

```bash
pytest tests/ --cov=src/python --cov-report=html
```

## 📝 Code Quality

### Format Code

```bash
# Format Python code
black src/python tests/

# Format C++ code
clang-format -i src/cpp/**/*.cpp src/cpp/**/*.h

# Organize imports
isort src/python tests/
```

### Type Checking

```bash
mypy src/python --ignore-missing-imports
```

### Linting

```bash
flake8 src/python tests/
pylint src/python
```

## 🔍 Debugging

### Debug Python

```bash
# Run with logging
python -c "import logging; logging.basicConfig(level=logging.DEBUG)" src/python/main.py

# Use pdb debugger
python -m pdb src/python/main.py
```

### Debug C++

```bash
# Build with debug symbols
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake --build . --config Debug

# Use Visual Studio debugger or gdb
gdb ./build/bin/app
```

## 📦 Building for Distribution

### Create Python Package

```bash
python setup.py sdist bdist_wheel
```

### Create Executable (PyInstaller)

```bash
piinstaller --onefile --windowed src/python/main.py
```

## 🔄 Workflow

### Feature Development

1. Create feature branch
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make changes and test
   ```bash
   pytest tests/
   ```

3. Format and lint
   ```bash
   black src/python
   mypy src/python
   ```

4. Commit and push
   ```bash
   git commit -am "Add feature: description"
   git push origin feature/my-feature
   ```

5. Create Pull Request on GitHub

## 📚 Architecture Overview

### Module Structure

- **ui/** - PyQt6 user interface components
- **core/** - Core engines (autoclicker, macros, hotkeys)
- **services/** - External API integration (Bazaar, Wiki)
- **models/** - Data models and structures
- **utils/** - Utilities and helpers

### Data Flow

```
UI (PyQt6)
  ↓
Core Services (Python)
  ↓
C++ Performance Layer (pybind11)
  ↓
Windows API / DirectX
```

## 🐛 Common Issues

### Issue: pybind11 not found

```bash
pip install pybind11
```

### Issue: CMake configuration fails

```bash
cmake --version  # Ensure 3.16+
pip install cmake
```

### Issue: Import errors in tests

```bash
# Ensure src/python is in path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src/python"
```

## 📖 Additional Resources

- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [pynput Documentation](https://pynput.readthedocs.io/)
- [CMake Documentation](https://cmake.org/documentation/)
- [pybind11 Documentation](https://pybind11.readthedocs.io/)

---

**For more details, see ARCHITECTURE.md and API.md**
