cmake_minimum_required(VERSION 3.10)

# Project name
project(LegoPlot)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(glfw3 REQUIRED)
find_package(OpenGL REQUIRED)

# Include directories
include_directories(inc)

# Add executable
add_executable(LegoPlot
    src/main.cpp
    src/Window.cpp
    src/Shader.cpp
)

# Link libraries
target_link_libraries(LegoPlot 
    glfw 
    OpenGL::GL
)

# Compiler-specific options
if(MSVC)
    target_compile_options(LegoPlot PRIVATE /W4)
else()
    target_compile_options(LegoPlot PRIVATE -Wall -Wextra -pedantic)
endif()