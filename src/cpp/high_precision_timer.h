#pragma once

#include <windows.h>
#include <chrono>

/**
 * High-precision timer for frame-perfect macro playback.
 */
class HighPrecisionTimer {
public:
    HighPrecisionTimer();

    /**
     * Start timing.
     */
    void start();

    /**
     * Get elapsed time in milliseconds.
     */
    double elapsed_ms() const;

    /**
     * Sleep for specified milliseconds with high precision.
     */
    static void precise_sleep(double ms);

private:
    std::chrono::high_resolution_clock::time_point _start_time;
};
