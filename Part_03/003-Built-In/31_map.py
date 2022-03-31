'''
    Applies a given function to each item of an iterable (list, tuple, set and dict) and returns an iterator.
'''

list_numbers    = [1, 2, 3, 4, 5, 6]
set_numbers     = {1, 2, 3, 4, 5, 6}
tuple_numbers   = (1, 2, 3, 4, 5, 6)
dict_numbers    = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6}

# regular function
def square(number): return number * number

print(f'List:   {list(map(square, list_numbers))}')
print(f'Set:    {list(map(square, set_numbers))}')
print(f'Tupple: {list(map(square, tuple_numbers))}')
print(f'Dict:   {list(map(square, dict_numbers.values()))}')

# lambda function
cube = lambda x: x * x * x

print(f'List:   {list(map(cube, list_numbers))}')
print(f'Set:    {list(map(cube, set_numbers))}')
print(f'Tupple: {list(map(cube, tuple_numbers))}')
print(f'Dict:   {list(map(cube, dict_numbers.values()))}')