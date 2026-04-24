#include "input_engine.h"
#include <iostream>

InputEngine::InputEngine() {
    // Initialize input engine
}

InputEngine::~InputEngine() {
    // Cleanup
}

void InputEngine::click(int x, int y, int button) {
    // Move to position
    move(x, y);

    INPUT inputs[2] = {};

    // Mouse button down
    inputs[0].type = INPUT_MOUSE;
    inputs[0].mi.dwFlags = (button == 0) ? MOUSEEVENTF_LEFTDOWN :
                            (button == 1) ? MOUSEEVENTF_RIGHTDOWN :
                            MOUSEEVENTF_MIDDLEDOWN;

    // Mouse button up
    inputs[1].type = INPUT_MOUSE;
    inputs[1].mi.dwFlags = (button == 0) ? MOUSEEVENTF_LEFTUP :
                            (button == 1) ? MOUSEEVENTF_RIGHTUP :
                            MOUSEEVENTF_MIDDLEUP;

    _send_input(inputs[0]);
    _send_input(inputs[1]);
}

void InputEngine::move(int x, int y) {
    INPUT input = {};
    input.type = INPUT_MOUSE;
    input.mi.dx = x;
    input.mi.dy = y;
    input.mi.dwFlags = MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE;

    _send_input(input);
}

void InputEngine::press_key(BYTE vk) {
    INPUT input = {};
    input.type = INPUT_KEYBOARD;
    input.ki.wVk = vk;
    input.ki.dwFlags = 0;

    _send_input(input);
}

void InputEngine::release_key(BYTE vk) {
    INPUT input = {};
    input.type = INPUT_KEYBOARD;
    input.ki.wVk = vk;
    input.ki.dwFlags = KEYEVENTF_KEYUP;

    _send_input(input);
}

void InputEngine::get_mouse_position(int& x, int& y) {
    POINT p;
    GetCursorPos(&p);
    x = p.x;
    y = p.y;
}

bool InputEngine::window_in_focus() {
    HWND foreground = GetForegroundWindow();
    HWND minecraft = FindWindowA(NULL, "Minecraft");
    return foreground == minecraft;
}

void InputEngine::_send_input(const INPUT& input) {
    SendInput(1, (LPINPUT)&input, sizeof(INPUT));
}
