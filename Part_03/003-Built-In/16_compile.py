'''
    Returns a Python code object.
'''

code = '''
a = 5
b = 2
print(f'{a} x {b} = {a * b}')
'''

compiledCode = compile(code, 'string', 'exec')

exec(compiledCode)