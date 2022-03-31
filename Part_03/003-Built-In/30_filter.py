'''
    Extracts elements from an iterable (list, tuple, set and dict) for which a function returns True.
'''

list_numbers    = [1, 2, 3, 4, 5, 6]
set_numbers     = {1, 2, 3, 4, 5, 6}
tuple_numbers   = (1, 2, 3, 4, 5, 6)
dict_numbers    = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6}

# regular function
def check_even(number):
    return True if number % 2 == 0 else False

print(f'List:   {list(filter(check_even, list_numbers))}')
print(f'Set:    {list(filter(check_even, set_numbers))}')
print(f'Tupple: {list(filter(check_even, tuple_numbers))}')
print(f'Dict:   {list(filter(check_even, dict_numbers.values()))}\n')

# lambda function
check_odd = lambda x: (x % 2 != 0)

print(f'List:   {list(filter(check_odd, list_numbers))}')
print(f'Set:    {list(filter(check_odd, set_numbers))}')
print(f'Tupple: {list(filter(check_odd, tuple_numbers))}')
print(f'Dict:   {list(filter(check_odd, dict_numbers.values()))}\n')