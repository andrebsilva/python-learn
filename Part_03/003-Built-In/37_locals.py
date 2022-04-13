'''
    Returns the dictionary of the current global symbol table.
'''

# Same globals()
print(locals(), '\n')
print(locals()['__file__'], '\n')

def actual_name():
    name = 'Jon'
    print(locals()['name'], '\n')
    return name

actual_name()

# print(locals()['name'], '\n')    # Error
