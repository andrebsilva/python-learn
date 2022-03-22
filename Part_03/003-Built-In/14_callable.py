'''
    Returns True if the object passed appears callable. If not, it returns False.
'''

num = 10

array = [0, 1, 2, 3]


print(callable(num))

print(callable(array))



value = lambda v: print(v)

def test():
    print('\nSome functions')

t = test

print(callable(value))

print(callable(test))

print(callable(t))


class Test:
    def __init__(self):
        print('\nSome Class')

t = Test

print(callable(Test))

print(callable(t))