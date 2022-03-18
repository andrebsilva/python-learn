'''
    Converts a value to Boolean (True od False)
'''

printer = lambda value: print(f'{value}', bool(value), sep = "\t")

printer(0)
printer(1)
printer(25)
printer([])
printer([0])
printer(None)
printer(True)
printer(False)
printer('Text')
