'''
    Adds a counter to an iterable and returns it (the enumerate object).
'''

names = ['Jon', 'Aleks', 'Ruy']

# c, counter
# i, iterator
for c, i in enumerate(names, 1):
    print(f'{c}: {i}')