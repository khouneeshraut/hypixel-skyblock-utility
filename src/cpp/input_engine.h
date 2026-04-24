#pragma once

#include <windows.h>
#include <functional>
#include <memory>
#include <atomic>
#include <thread>

/**
 * High-performance input engine for Windows platform.
 * Handles low-level mouse and keyboard input operations.
 */
class InputEngine {
public:
    InputEngine();
    ~InputEngine();

    /**
     * Click at specified coordinates.
     * @param x X coordinate
     * @param y Y coordinate
     * @param button Mouse button (0=left, 1=right, 2=middle)
     */
    void click(int x, int y, int button = 0);

    /**
     * Move mouse to position.
     */
    void move(int x, int y);

    /**
     * Press a key.
     * @param vk Virtual key code
     */
    void press_key(BYTE vk);

    /**
     * Release a key.
     */
    void release_key(BYTE vk);

    /**
     * Get current mouse position.
     */
    void get_mouse_position(int& x, int& y);

    /**
     * Check if window has focus.
     */
    bool window_in_focus();

private:
    void _send_input(const INPUT& input);
};
