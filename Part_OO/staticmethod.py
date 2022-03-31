'''
    Returns a static method for a given function.
'''
class Test:
    def __init__(self, *numbers):
        self.numbers = list(numbers) if type(numbers) is tuple else numbers
    
    def sum_all_numbers(self):
        return sum(self.numbers)

    # @staticmethod
    def sum(*numbers):
        result = 0
        for i in numbers: result += i
        return result
        

test_1 = Test(1, 2, 3, 3)

print(f'Classmethod : Result = {test_1.sum_all_numbers()}')

print(f'Staticmethod: Result = {Test.sum(2, 3, 4, 4)}')

test_1.sum = staticmethod(Test.sum)

print(f'Staticmethod: Result = {test_1.sum(2, 3, 4, 4)}') # Error

