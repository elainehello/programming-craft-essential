l: list[int] = [2, 3, 4, 6, 9, 11, 13, 14, 15, 18]
"""
binary search on sorted list
"""
search_for = 14
slice_start: int = 0
slice_end: int = len(l) - 1
found = False

while slice_start <= slice_end and not found:
    location = (slice_start + slice_end) // 2
    if l[location] == search_for:
        found = True
    else:
        if search_for < l[location]:
            slice_end = location - 1
        else:
            slice_start = location + 1
print(found)
print(location)
