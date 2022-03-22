'''
    Returns a bytearray object which is an array of the given bytes.
'''

number = 4

array = [1, 2, 5, 16]


print(bytearray(array))

print(bytearray(number))

print(bytearray('Some text', 'utf-8'))