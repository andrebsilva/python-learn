size = 5

for x in range(size):
    for y in range(size):
        if x == y or x + y == size - 1:
            print(f'x', end = '\t')
        else:
            print(f' ', end = '\t')
    print("\n")