'''
    Returns the dictionary of the current global symbol table.
'''

year = 2022

print(globals(), '\n')
print(globals()['__file__'], '\n')
print(globals()['year'], '\n')

def actual_name():
    name = 'Jon'
    print(globals()['name'], '\n')
    return name

# actual_name()     # Error

# print(globals()['name'], '\n')    # Error