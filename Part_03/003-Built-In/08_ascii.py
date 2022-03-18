'''
    Returns a string containing a printable representation of an object.
'''

printer = lambda value: print(f'{value} ->', ascii(value), sep = "\t")

printer('a e i o u')

printer('à ê í õ ü')

printer(['São', 'José'])

print('\u221a A\xe7\xe3o')