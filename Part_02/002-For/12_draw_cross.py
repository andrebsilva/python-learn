size = 4

if size % 2 == 0:
    for x in range(size + 1):
        for y in range(size + 1):
            if x == size // 2 or y == size // 2:
                print(f'x', end = ' ')
            else:
                print(f' ', end = ' ')
        print(end = '\n')
else:
    for x in range(size):
        for y in range(size):
            if x == size // 2 or y == size // 2:
                print(f'x', end = ' ')
            else:
                print(f' ', end = ' ')
        print(end = '\n')