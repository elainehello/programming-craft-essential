#!/bin/bash

# Test script for 01_find_max program
# Generates random numbers and tests the max_of_four function

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Function to print test results
print_result() {
    local test_name="$1"
    local expected="$2"
    local actual="$3"
    local input="$4"
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    if [ "$expected" -eq "$actual" ]; then
        echo -e "${GREEN}✓ PASS${NC} - $test_name"
        echo -e "  Input: $input"
        echo -e "  Expected: $expected, Got: $actual"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo -e "${RED}✗ FAIL${NC} - $test_name"
        echo -e "  Input: $input"
        echo -e "  Expected: $expected, Got: $actual"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    echo
}

# Function to find max of 4 numbers (for verification)
find_max() {
    local max=$1
    for num in "$@"; do
        if [ "$num" -gt "$max" ]; then
            max=$num
        fi
    done
    echo $max
}

# Function to run test
run_test() {
    local test_name="$1"
    local a="$2"
    local b="$3"
    local c="$4"
    local d="$5"
    
    # Calculate expected result
    local expected=$(find_max $a $b $c $d)
    
    # Run the program and capture output
    local output=$(echo "$a $b $c $d" | ./01_find_max 2>/dev/null)
    local actual=$(echo "$output" | grep -o '[0-9-]*' | tail -1)
    
    print_result "$test_name" "$expected" "$actual" "$a $b $c $d"
}

echo -e "${YELLOW}=== Testing 01_find_max Program ===${NC}"
echo

# Compile the program first
echo "Compiling program..."
if g++ -o 01_find_max 01_find_max.cpp 2>/dev/null; then
    echo -e "${GREEN}Compilation successful${NC}"
else
    echo -e "${RED}Compilation failed!${NC}"
    exit 1
fi
echo

# Test 1: Known values
echo -e "${YELLOW}--- Basic Tests ---${NC}"
run_test "Basic test 1" 1 4 8 0
run_test "Basic test 2" 10 3 15 7
run_test "All same numbers" 5 5 5 5
run_test "Negative numbers" -1 -4 -8 0

# Test 2: Edge cases
echo -e "${YELLOW}--- Edge Cases ---${NC}"
run_test "All negative" -10 -5 -15 -3
run_test "Large numbers" 1000000 999999 1000001 500000
run_test "First is max" 100 1 2 3
run_test "Last is max" 1 2 3 100
run_test "Mixed signs" -50 25 -10 75

# Test 3: Random tests
echo -e "${YELLOW}--- Random Number Tests ---${NC}"
for i in {1..10}; do
    # Generate 4 random numbers between -100 and 100
    a=$((RANDOM % 201 - 100))
    b=$((RANDOM % 201 - 100))
    c=$((RANDOM % 201 - 100))
    d=$((RANDOM % 201 - 100))
    
    run_test "Random test $i" $a $b $c $d
done

# Test 4: Stress test with larger random numbers
echo -e "${YELLOW}--- Stress Tests ---${NC}"
for i in {1..5}; do
    # Generate 4 random numbers between -10000 and 10000
    a=$((RANDOM % 20001 - 10000))
    b=$((RANDOM % 20001 - 10000))
    c=$((RANDOM % 20001 - 10000))
    d=$((RANDOM % 20001 - 10000))
    
    run_test "Stress test $i" $a $b $c $d
done

# Summary
echo -e "${YELLOW}=== Test Summary ===${NC}"
echo "Total tests: $TOTAL_TESTS"
echo -e "Passed: ${GREEN}$PASSED_TESTS${NC}"
echo -e "Failed: ${RED}$FAILED_TESTS${NC}"

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}All tests passed! 🎉${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed! 😞${NC}"
    exit 1
fi
