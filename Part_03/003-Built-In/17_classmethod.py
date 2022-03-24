class Test:
    def sum_all(self, value):
        print(value + value)

Test.sum_all(1)

Test.new_sum_all = classmethod(Test.sum_all)

Test.new_sum_all(5)
