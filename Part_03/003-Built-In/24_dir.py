'''
    Tries to return a list of valid attributes of the object.
'''

class Test:
    def __dir__(self):
        return ['year', 'month', 'day']

# print(dir(Test))

t = Test()

print(dir(t))