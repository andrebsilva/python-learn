'''
    Returns a class method for the given function.
'''

class Test:
    def sum_all(self, value):
        print(value + value)

Test.new_sum_all = classmethod(Test.sum_all)

Test.new_sum_all(5)
