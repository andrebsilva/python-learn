'''
    Returns the binary of a given number.
'''
printer = lambda value: print(f'{value} ->', bin(value), sep = "\t")

class MyNumbers:
    
    first_number = 5
    second_number = 12
    
    def __index__(self):
        return self.first_number + self.second_number

printer(MyNumbers())