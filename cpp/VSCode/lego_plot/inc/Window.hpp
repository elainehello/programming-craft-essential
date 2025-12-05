#pragma once
#include <GLFW/glfw3.h>
#include <string>

namespace core
{
    class Window
    {
    public:
        Window(int width, int height, const std::string &title);
        ~Window(); // destructor declaration

        void pollEvents();
        void swapBuffers();
        bool shouldClose() const;

        GLFWwindow *get() const
        {
            return m_window;
        }

    private:
        GLFWwindow *m_window = nullptr;
        int m_width;
        int m_height;
        std::string m_title;
    };
} // namespace core
