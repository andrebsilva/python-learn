'''
    Adds a counter to an iterable and returns it (the enumerate object).
'''

years = [2001, 1998, 2006]

print(list(enumerate(years, start = 101)))
print(set(enumerate(years, start = 101)))
print(tuple(enumerate(years, 101)))
print(dict(enumerate(years, 101)))