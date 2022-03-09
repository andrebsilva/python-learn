# Perfect   - The sum of the divisors is equal to the number        [06]
# Deficient - The sum of the divisors is less than the number       [09]
# Abundant  - The sum of the divisors is greater than the number    [12]

sum = 0
number = eval(input("Number:\t"))

for i in range(1, number):
    if number % i == 0:
        sum += i

if number == sum:
    print(f'{number} is Perfect \t - Sum: {sum}')
elif number > sum:
    print(f'{number} is Deficient \t - Sum: {sum}')
else:
    print(f'{number} is Abundant \t - Sum: {sum}')