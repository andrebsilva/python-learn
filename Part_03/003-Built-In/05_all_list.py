'''
    Returns True if all element of a iterable is True. if not, it returns False.
    any(iterable)
'''

printer = lambda value: print(f'{value} ->', all(value), sep = "\t")

printer([0, 1])
printer([1, -5])
printer([False, False])
printer([False, True])
printer([True, True])

