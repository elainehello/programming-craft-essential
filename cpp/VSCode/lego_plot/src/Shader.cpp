#include "../inc/Shader.hpp"
#include <glad/glad.h> // GLAD must be included before other OpenGL headers
#include <fstream>
#include <sstream>
#include <iostream>

namespace core
{
    // Constructor
    Shader::Shader(const std::string &vertexPath, const std::string &fragmentPath)
    {
        // Load shader code
        std::string vertexCode = loadFile(vertexPath);
        std::string fragmentCode = loadFile(fragmentPath);

        // Compile shaders
        unsigned int vertex = compileShader(GL_VERTEX_SHADER, vertexCode.c_str());
        unsigned int fragment = compileShader(GL_FRAGMENT_SHADER, fragmentCode.c_str());

        // Link program
        ID = linkProgram(vertex, fragment);

        // Clean up shader objects
        glDeleteShader(vertex);
        glDeleteShader(fragment);
    }

    // Use Program
    void Shader::use() const
    {
        glUseProgram(ID);
    }

    // Uniform helper functions
    void Shader::setBool(const std::string &name, bool value) const
    {
        glUniform1i(glGetUniformLocation(ID, name.c_str()), (int)value);
    }

    void Shader::setInt(const std::string &name, int value) const
    {
        glUniform1i(glGetUniformLocation(ID, name.c_str()), value);
    }

    void Shader::setFloat(const std::string &name, float value) const
    {
        glUniform1f(glGetUniformLocation(ID, name.c_str()), value);
    }

    void Shader::setVec3(const std::string &name, const glm::vec3 &value) const
    {
        glUniform3fv(glGetUniformLocation(ID, name.c_str()), 1, &value[0]);
    }

    void Shader::setMat4(const std::string &name, const glm::mat4 &mat) const
    {
        glUniformMatrix4fv(glGetUniformLocation(ID, name.c_str()), 1, GL_FALSE, &mat[0][0]);
    }

    // Helper: load file
    std::string Shader::loadFile(const std::string &path)
    {
        std::ifstream file(path);
        std::stringstream buffer;

        if (!file.is_open())
        {
            std::cerr << "ERROR::SHADER: Failed to open file: " << path << std::endl;
            return "";
        }

        buffer << file.rdbuf();
        file.close();
        return buffer.str();
    }

    // Helper: compile shader
    unsigned int Shader::compileShader(unsigned int type, const char *source)
    {
        unsigned int shader = glCreateShader(type);
        glShaderSource(shader, 1, &source, nullptr);
        glCompileShader(shader);

        // Check for compilation errors
        checkCompileErrors(shader, (type == GL_VERTEX_SHADER) ? "VERTEX" : "FRAGMENT");

        return shader;
    }

    // Helper: link program
    unsigned int Shader::linkProgram(unsigned int vertex, unsigned int fragment)
    {
        unsigned int program = glCreateProgram();
        glAttachShader(program, vertex);
        glAttachShader(program, fragment);
        glLinkProgram(program);

        // Check for linking errors
        checkCompileErrors(program, "PROGRAM");

        return program;
    }

    // Helper: check for shader errors
    void Shader::checkCompileErrors(unsigned int shader, const std::string &type)
    {
        int success;
        char infoLog[MAX_BUFFER_SIZE];

        if (type != "PROGRAM")
        {
            glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
            if (!success)
            {
                glGetShaderInfoLog(shader, MAX_BUFFER_SIZE, nullptr, infoLog);
                std::cerr << "ERROR::SHADER_COMPILATION (" << type << "):\n"
                          << infoLog << "\n";
            }
        }
        else
        {
            glGetProgramiv(shader, GL_LINK_STATUS, &success);
            if (!success)
            {
                glGetProgramInfoLog(shader, MAX_BUFFER_SIZE, nullptr, infoLog);
                std::cerr << "ERROR::PROGRAM_LINKING:\n"
                          << infoLog << "\n";
            }
        }
    }

} // namespace core
