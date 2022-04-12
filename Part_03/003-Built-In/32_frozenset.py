'''
    Returns an immutable frozenset object initialized with elements from the given iterable.
'''

names = ['Jon', 'Aleks', 'Ruy']

names.append('Mary')

print(names)


fruits = frozenset(['Apple', 'Banana', 'Orange'])

# fruits.append('Lemon')

print(fruits)