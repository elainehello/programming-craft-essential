from typing import List

def findSmaller(arr: List[int]) -> int:
    if not arr:
        raise ValueError("arr must not be empty")
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr: List[int]) -> List[int]:
    new_arr: List[int] = []
    copied_arr = list(arr)

    while copied_arr:
        smallest = findSmaller(copied_arr)
        new_arr.append(copied_arr.pop(smallest))
    return new_arr

print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([]))
