l: list[int] = [80, 5, 4, 7, 10, 2]

search_for = 7
result = -1
value = 0
for i in range(len(l)):
    if search_for == l[i]:
        result = i
        value = l[i]
        break

print(f"[Index position]: {result} [value found]: {value}")
