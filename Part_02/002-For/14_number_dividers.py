# All numbers with the same number of divisors, until 1000

dividers = eval(input('Number of dividers [2 to 32]: '))
size = 1000

for i in range(1, size + 1):
    aux = 1
    for j in range(1, i):
        if i % j == 0:
            aux += 1
    if aux == dividers:
        print(f'{aux} Dividers: {i}')