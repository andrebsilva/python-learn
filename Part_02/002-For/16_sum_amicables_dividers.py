# Amicable
# The sum of the dividers is equal to other number
# And the sum of this another number is equal to the first number

size = 20_000
start = 1

for number in range(start, size):
    
    sum_i = 0

    for i in range(1, number):
        if number % i == 0:
            sum_i += i

    sum_j = 0

    for j in range(1, sum_i):
        if sum_i % j == 0:
            sum_j += j

    if number == sum_j and number != sum_i and sum_j < sum_i:
        print(f'{number} is Amicable to {sum_i}')
