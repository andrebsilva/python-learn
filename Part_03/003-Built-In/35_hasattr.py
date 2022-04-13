'''
    Returns true if an object has the given named attribute and false if it does not.
'''

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

uno = Car('Uno', 1998)

print(hasattr(uno, 'model'))

print(hasattr(uno, 'year'))