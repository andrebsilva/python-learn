from simple_class import Test


obj = Test('Jon', 'Doe')
print(obj.get_complete_name())

obj.__set_first_name('Harry') # ERROR
print(f'{obj.get_first_name()} {obj.get_last_name()}')