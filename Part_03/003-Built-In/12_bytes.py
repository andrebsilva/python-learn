'''
    Returns a immutable bytes object initialized with the given size and data.
'''

number = 4

array = [1, 2, 5, 16]


print(bytes(array))

print(bytes(number))

print(bytes('Some text', 'utf-8'))