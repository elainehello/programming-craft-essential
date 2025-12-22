
# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c99

# Target executable name
TARGET = program

# Object directory
OBJ_DIR = obj

# Source files
SOURCES = main.c arithmetic_op.c

# Object files (automatically generated from sources)
OBJECTS = $(SOURCES:%.c=$(OBJ_DIR)/%.o)

# Default target
all: $(TARGET)

# Build the executable
$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(TARGET) -lm

# Create object directory if it doesn't exist
$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

# Compile source files to object files
$(OBJ_DIR)/%.o: %.c core.h | $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up generated files
clean:
	rm -rf $(OBJ_DIR) $(TARGET) valgrind.log

# Rebuild everything
rebuild: clean all

# Run with valgrind to check for memory leaks
valgrind: $(TARGET)
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --verbose ./$(TARGET)

# Run with valgrind and save output to file
valgrind-log: $(TARGET)
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --verbose --log-file=valgrind.log ./$(TARGET)

# Mark targets that don't create files
.PHONY: all clean rebuild valgrind valgrind-log