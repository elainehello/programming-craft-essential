#!/usr/bin/env python3

import math

total: int = 0
numbers: list[int] = [8, 5, 1]
for n in numbers:
    total += math.factorial(n)
print(total)