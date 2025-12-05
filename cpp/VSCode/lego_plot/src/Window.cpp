#include "../inc/Window.hpp"
#include <iostream>
#include <cstdlib>
#include <GL/gl.h>

namespace core
{
    Window::Window(int width, int height, const std::string &title)
        : m_width(width), m_height(height), m_title(title)
    {
        int init_glfw = glfwInit();

        if (!init_glfw)
        {
            std::cerr << "Failed to initialize the GLFW library.\n";
            std::exit(EXIT_FAILURE);
        }

        // Sets the specified window hint to the desired value.
        glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
        glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);
        glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_ANY_PROFILE);

        std::cout << "Creating GLFW window..." << std::endl;
        // Creates a window and its associated context.
        m_window = glfwCreateWindow(width, height, title.c_str(), nullptr, nullptr); // c_str() does pointer to an array convertion
        if (!m_window)
        {
            std::cerr << "Failed to create GLFW window.\n";
            std::exit(EXIT_FAILURE);
        }

        // Center the window
        // glfwGetPrimaryMonitor() Returns the primary monitor.
        GLFWmonitor *monitor = glfwGetPrimaryMonitor();
        // glfwGetVideoMode - Returns the available video modes for the specified monitor
        const GLFWvidmode *mode = glfwGetVideoMode(monitor);
        int x_axis = (mode->width - width) / 2;
        int y_axis = (mode->height - height) / 2;
        glfwSetWindowPos(m_window, x_axis, y_axis); // Makes the context of the specified window current for the calling thread.
        glfwMakeContextCurrent(m_window);

        std::cout << "Window setup complete!" << std::endl;
    }

    Window::~Window()
    {
        if (m_window)
        {
            glfwDestroyWindow(m_window);
        }
        glfwTerminate();
    }

    void Window::pollEvents()
    {
        glfwPollEvents();
    }

    void Window::swapBuffers()
    {
        glfwSwapBuffers(m_window);
    }

    bool Window::shouldClose() const
    {
        return glfwWindowShouldClose(m_window);
    }

} // namespace core
