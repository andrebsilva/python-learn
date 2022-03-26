'''
    Deletes an attribute from the object, if the object allows it.
'''

class Test:
    
    age = 20
    name = 'Jon'
    birth_year = 2002
     
    def __init__(self):
        print(f'Age       : {self.age}')
        print(f'Name      : {self.name}')
        print(f'Birth Year: {self.birth_year}')

Test()

delattr(Test, 'age')

Test()    # Error: Object has no attribute age