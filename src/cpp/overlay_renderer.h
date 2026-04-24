#pragma once

#include <windows.h>
#include <d3d11.h>
#include <string>
#include <memory>

#pragma comment(lib, "d3d11.lib")
#pragma comment(lib, "dxgi.lib")

/**
 * DirectX 11 based overlay renderer for always-on-top window.
 */
class OverlayRenderer {
public:
    OverlayRenderer();
    ~OverlayRenderer();

    /**
     * Initialize overlay window and DirectX.
     */
    bool initialize();

    /**
     * Show overlay.
     */
    void show();

    /**
     * Hide overlay.
     */
    void hide();

    /**
     * Toggle overlay visibility.
     */
    void toggle();

    /**
     * Draw text on overlay.
     */
    void draw_text(const std::string& text, float x, float y);

    /**
     * Clear overlay.
     */
    void clear();

    /**
     * Present frame.
     */
    void present();

    /**
     * Check if overlay is visible.
     */
    bool is_visible() const;

private:
    HWND _hwnd = nullptr;
    ID3D11Device* _device = nullptr;
    ID3D11DeviceContext* _context = nullptr;
    IDXGISwapChain* _swap_chain = nullptr;
    ID3D11RenderTargetView* _rtv = nullptr;
    bool _visible = false;

    bool _create_window();
    bool _setup_directx();
    void _cleanup();
};
