cmake_minimum_required(VERSION 3.16)
project(hypixel_core)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

# Source files
set(SOURCES
    input_engine.cpp
    overlay_renderer.cpp
    bindings.cpp
)

set(HEADERS
    input_engine.h
    overlay_renderer.h
    high_precision_timer.h
)

# Create pybind11 module
pybind11_add_module(hypixel_core ${SOURCES} ${HEADERS})

# Link Windows libraries
if(WIN32)
    target_link_libraries(hypixel_core PRIVATE
        user32 kernel32 winmm
        d3d11 dxgi
    )
endif()

# Set output directory
set_target_properties(hypixel_core PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)
