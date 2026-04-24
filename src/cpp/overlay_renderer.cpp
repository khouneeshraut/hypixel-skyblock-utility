#include "overlay_renderer.h"
#include <iostream>

OverlayRenderer::OverlayRenderer() = default;

OverlayRenderer::~OverlayRenderer() {
    _cleanup();
}

bool OverlayRenderer::initialize() {
    if (!_create_window()) {
        return false;
    }

    if (!_setup_directx()) {
        return false;
    }

    return true;
}

void OverlayRenderer::show() {
    if (_hwnd) {
        ShowWindow(_hwnd, SW_SHOW);
        _visible = true;
    }
}

void OverlayRenderer::hide() {
    if (_hwnd) {
        ShowWindow(_hwnd, SW_HIDE);
        _visible = false;
    }
}

void OverlayRenderer::toggle() {
    if (_visible) {
        hide();
    } else {
        show();
    }
}

void OverlayRenderer::draw_text(const std::string& text, float x, float y) {
    // Implementation for drawing text
    // This would use DirectWrite for text rendering
}

void OverlayRenderer::clear() {
    if (!_context || !_rtv) return;

    float clear_color[4] = {0.0f, 0.0f, 0.0f, 0.0f};
    _context->ClearRenderTargetView(_rtv, clear_color);
}

void OverlayRenderer::present() {
    if (_swap_chain) {
        _swap_chain->Present(1, 0);
    }
}

bool OverlayRenderer::is_visible() const {
    return _visible;
}

bool OverlayRenderer::_create_window() {
    // Create invisible layered window for overlay
    // Implementation details...
    return true;
}

bool OverlayRenderer::_setup_directx() {
    // Setup DirectX 11 device and swap chain
    // Implementation details...
    return true;
}

void OverlayRenderer::_cleanup() {
    if (_rtv) {
        _rtv->Release();
        _rtv = nullptr;
    }
    if (_swap_chain) {
        _swap_chain->Release();
        _swap_chain = nullptr;
    }
    if (_context) {
        _context->Release();
        _context = nullptr;
    }
    if (_device) {
        _device->Release();
        _device = nullptr;
    }
}
