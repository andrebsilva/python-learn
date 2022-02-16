'''
Error tests:
    Hello
    true
    false
    none
Tests:
    'Hello'
    True
    False
    None
    10
    10.5
    [1, 2, 3]
    (1, 2, 3)
    {1, 2, 3}
    {'a': 1, 'b': 2, 'c': 3}
'''

value = eval(input("Value: "))

print("Value =", value)
print("Type  =", type(value))
