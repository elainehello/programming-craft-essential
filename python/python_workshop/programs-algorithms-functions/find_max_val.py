listNbr: list[int] = [5, 0, 6, 9, 7, 4]

# Initialize max_nbr to first element to handle negative numbers correctly
max_nbr = listNbr[0]
for nbr in listNbr:
    if nbr > max_nbr:
        max_nbr = nbr
print(max_nbr)