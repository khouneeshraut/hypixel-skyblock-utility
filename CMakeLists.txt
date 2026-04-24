cmake_minimum_required(VERSION 3.16)
project(hypixel_skyblock_utility)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# Find pybind11
find_package(pybind11 REQUIRED)

# Find required libraries for Windows
if(WIN32)
    set(WINDOWS_LIBS user32 kernel32 winmm)
endif()

# Add C++ source files
set(CPP_SOURCES
    src/cpp/input_engine.cpp
    src/cpp/overlay_renderer.cpp
    src/cpp/bindings.cpp
)

set(CPP_HEADERS
    src/cpp/input_engine.h
    src/cpp/overlay_renderer.h
    src/cpp/high_precision_timer.h
)

# Create pybind11 module
pybind11_add_module(hypixel_core ${CPP_SOURCES} ${CPP_HEADERS})

# Link Windows libraries
if(WIN32)
    target_link_libraries(hypixel_core PRIVATE ${WINDOWS_LIBS})
endif()

# Set output directory
set_target_properties(hypixel_core PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)

# Enable testing
enable_testing()
add_subdirectory(tests)
