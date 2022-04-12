'''
    Returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
'''

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

uno = Car('Uno', 1998)

print(uno.model)
print(getattr(uno, 'model'))

print(uno.year)
print(getattr(uno, 'year'))