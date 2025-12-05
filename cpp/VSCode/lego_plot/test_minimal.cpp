#include <GLFW/glfw3.h>
#include <iostream>

int main() {
    std::cout << "Initializing GLFW..." << std::endl;
    
    if (!glfwInit()) {
        std::cout << "Failed to initialize GLFW" << std::endl;
        return -1;
    }
    
    std::cout << "GLFW initialized successfully" << std::endl;
    
    // Set window hints for compatibility
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 2);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1);
    
    std::cout << "Creating window..." << std::endl;
    GLFWwindow* window = glfwCreateWindow(640, 480, "Test", NULL, NULL);
    
    if (!window) {
        std::cout << "Failed to create window" << std::endl;
        glfwTerminate();
        return -1;
    }
    
    std::cout << "Window created successfully!" << std::endl;
    
    glfwDestroyWindow(window);
    glfwTerminate();
    
    std::cout << "Cleanup complete" << std::endl;
    return 0;
}
