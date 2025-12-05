#include "../inc/Window.hpp"
#include <iostream>
#include <string>
#include <GL/gl.h>

int main()
{
    std::cout << "Starting application..." << std::endl;

    int width = 800;
    int height = 600;
    std::string title = "Lego Plot";

    std::cout << "Creating window..." << std::endl;
    core::Window window(width, height, title);
    std::cout << "Window created successfully!" << std::endl;

    // Main loop
    std::cout << "Entering main loop..." << std::endl;
    while (!window.shouldClose())
    {
        // Poll for and process events
        window.pollEvents();

        // Swap front and back buffers
        window.swapBuffers();
    }

    std::cout << "Exiting application..." << std::endl;

    return 0;
}
