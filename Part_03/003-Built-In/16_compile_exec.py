'''
    Returns a Python code object.
'''

code = '''
a = 5
b = 2
print(f'{a} x {b} = {a * b}')
'''

compiledCode = compile(code, 'string', 'exec')

'''
    Executes the dynamically created program, which is either a string or a code object.
'''

exec(compiledCode)

exec('num_a = 6\nnum_b = 8\nprint(num_a, " + ", num_b, " = ", num_a + num_b)')