'''
    Takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
'''

names = ['Jon', 'Aleks', 'Ruy']

years = [2001, 1998, 2006]

print(list(zip(names, years)))