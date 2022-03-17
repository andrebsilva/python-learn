'''
    Returns the binary of a given number.
'''

class MyNumbers:
    
    first_number = 10
    second_number = 20
    third_number = 25
    
    def __index__(self):
        return self.first_number + self.second_number + self.third_number

print(bin(MyNumbers()))