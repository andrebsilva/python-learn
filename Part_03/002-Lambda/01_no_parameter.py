'''
    Built-in function: globals()
    Returns the dictionary of the current global symbol table.
'''

path_globals = lambda: globals()['__file__']

print(path_globals())