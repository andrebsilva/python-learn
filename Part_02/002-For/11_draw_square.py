size = 4

for x in range(size):
    for y in range(size):
        if x == size - size or y == size - size or x == size - 1 or y == size - 1:
            print(f'x', end = '\t')
        else:
            print(f' ', end = '\t')
    print("\n")