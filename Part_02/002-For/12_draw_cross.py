size = 2

if size % 2 == 0:
    size += 1
    for x in range(size):
        for y in range(size):
            if x == (size - 1) / 2 or y == (size - 1) / 2:
                print(f'x', end = '\t')
            else:
                print(f' ', end = '\t')
        print("\n")
