# All divisor og a number

number = eval(input("Number:\t"))

for i in range(1, number + 1):
    if number % i == 0: print(i)
    