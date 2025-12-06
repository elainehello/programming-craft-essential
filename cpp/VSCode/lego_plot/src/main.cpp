#include "../inc/Window.hpp"
#include "../inc/Shader.hpp"
#include <glad/glad.h> // GLAD must be included before other OpenGL headers
#include <iostream>
#include <string>

int main()
{
    std::cout << "Starting application..." << std::endl;

    int width = 800;
    int height = 600;
    std::string title = "Lego Plot - Shader Test";

    std::cout << "Creating window..." << std::endl;
    core::Window window(width, height, title);
    std::cout << "Window created successfully!" << std::endl;

    // Test Shader class
    std::cout << "\n=== Testing Shader Class ===" << std::endl;
    try
    {
        core::Shader testShader("shaders/vertex.glsl", "shaders/fragment.glsl");
        std::cout << "\nShader created successfully! ID: " << testShader.ID << std::endl;

        // Test using the shader
        std::cout << "\nTesting shader usage..." << std::endl;
        testShader.use();

        // Test setting uniforms
        std::cout << "\nTesting uniform setters..." << std::endl;
        testShader.setFloat("testFloat", 1.5f);
        testShader.setInt("testInt", 42);
        testShader.setBool("testBool", true);

        // Test GLM types
        glm::vec3 testVec(1.0f, 2.0f, 3.0f);
        testShader.setVec3("testVec3", testVec);

        glm::mat4 testMat(1.0f); // Identity matrix
        testShader.setMat4("testMat4", testMat);

        std::cout << "\nAll shader tests completed successfully!" << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Shader test failed: " << e.what() << std::endl;
    }

    std::cout << "\n=== Entering Main Loop ===" << std::endl;
    // Main loop
    while (!window.shouldClose())
    {
        // Clear screen with a nice color
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        // Poll for and process events
        window.pollEvents();

        // Swap front and back buffers
        window.swapBuffers();
    }

    std::cout << "Exiting application..." << std::endl;
    return 0;
}
