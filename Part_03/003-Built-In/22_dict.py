'''
    This constructor creates a dictionary in Python.
'''

names = ['Jon', 'Aleks', 'Ruy']

years = [2001, 1998, 2006]

print(list(zip(names, years)))
print(set(zip(names, years)))
print(tuple(zip(names, years)))
print(dict(zip(names, years)))