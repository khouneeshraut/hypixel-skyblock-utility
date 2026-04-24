#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include "input_engine.h"
#include "overlay_renderer.h"
#include "high_precision_timer.h"

namespace py = pybind11;

/**
 * Pybind11 bindings for C++ components.
 * This allows Python to use the high-performance C++ implementations.
 */
PYBIND11_MODULE(hypixel_core, m) {
    m.doc() = "Hypixel SkyBlock Utility C++ Core";

    // InputEngine bindings
    py::class_<InputEngine>(m, "InputEngine")
        .def(py::init<>())
        .def("click", &InputEngine::click, "Click at position")
        .def("move", &InputEngine::move, "Move mouse")
        .def("press_key", &InputEngine::press_key, "Press key")
        .def("release_key", &InputEngine::release_key, "Release key")
        .def("get_mouse_position", &InputEngine::get_mouse_position, "Get mouse position")
        .def("window_in_focus", &InputEngine::window_in_focus, "Check if Minecraft window is focused");

    // OverlayRenderer bindings
    py::class_<OverlayRenderer>(m, "OverlayRenderer")
        .def(py::init<>())
        .def("initialize", &OverlayRenderer::initialize, "Initialize overlay")
        .def("show", &OverlayRenderer::show, "Show overlay")
        .def("hide", &OverlayRenderer::hide, "Hide overlay")
        .def("toggle", &OverlayRenderer::toggle, "Toggle overlay visibility")
        .def("draw_text", &OverlayRenderer::draw_text, "Draw text on overlay")
        .def("clear", &OverlayRenderer::clear, "Clear overlay")
        .def("present", &OverlayRenderer::present, "Present frame")
        .def("is_visible", &OverlayRenderer::is_visible, "Check if overlay is visible");

    // HighPrecisionTimer bindings
    py::class_<HighPrecisionTimer>(m, "HighPrecisionTimer")
        .def(py::init<>())
        .def("start", &HighPrecisionTimer::start, "Start timer")
        .def("elapsed_ms", &HighPrecisionTimer::elapsed_ms, "Get elapsed milliseconds")
        .def_static("precise_sleep", &HighPrecisionTimer::precise_sleep, "Sleep with high precision");
}
