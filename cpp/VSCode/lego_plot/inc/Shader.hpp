#pragma once
#include <string>
#include <glm/glm.hpp>
constexpr std::size_t MAX_BUFFER_SIZE = 1024;

namespace core
{
    class Shader
    {
    public:
        unsigned int ID;

        Shader(const std::string &vertexPath, const std::string &fragmentPath);
        void use() const;

        // Uniform helpers
        void setBool(const std::string &name, bool value) const;
        void setInt(const std::string &name, int value) const;
        void setFloat(const std::string &name, float value) const;
        void setVec3(const std::string &name, const glm::vec3 &value) const;
        void setMat4(const std::string &name, const glm::mat4 &mat) const;

    private:
        // File loading
        std::string loadFile(const std::string &path);

        // Shader compilation and linking
        unsigned int compileShader(unsigned int type, const char* source);
        unsigned int linkProgram(unsigned int vertex, unsigned int fragment);

        //Error Checking
        void checkCompileErrors(unsigned int shader, const std::string &type);
        
    };
} // namespace core
