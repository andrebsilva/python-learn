def my_own_function(first_name, last_name = '\b'):
    return f'Hello, {first_name} {last_name}!'

print(my_own_function('Jon', 'Doe'))
print(my_own_function('Jon'))
