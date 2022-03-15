def records(**values):
    return f"Hello, {values['first_name']} {values['last_name']}!"

print(records(first_name = 'Jon', last_name = 'Doe',))
print(records(**{"first_name": 'Jon', "last_name": 'Doe'}))
print(records(**{"first_name": 'Jon'}, **{"last_name": 'Doe'}))
