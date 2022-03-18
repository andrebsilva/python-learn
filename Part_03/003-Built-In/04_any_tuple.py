'''
    Returns True if any element of a iterable is True. if not, it returns False.
    any(iterable)
'''

printer = lambda value: print(f'{value} ->', any(value), sep = "\t")

printer((0, 0))
printer((0, 1))
printer((0, -9, 0))
printer((False, False))
printer((False, True))