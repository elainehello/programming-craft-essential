l: list[int] = [80, 5, 4, 7, 10, 2]

still_swapping = True
while still_swapping:
    still_swapping = False
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            still_swapping = True
print(l)
