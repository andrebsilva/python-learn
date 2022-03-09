# Number of dividers

dividers = eval(input('Number of dividers [2 to 32]: '))
size = 1000

for i in range(1, size + 1):
    a = 1
    for j in range(1, i):
        if i % j == 0:
            a += 1
    if a == dividers:
        print(f'{a} Dividers: {i}')