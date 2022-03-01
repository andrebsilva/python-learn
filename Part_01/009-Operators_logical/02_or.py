first_number = eval(input("Number:\t"))
second_number = eval(input("Number:\t"))
third_number = eval(input("Number:\t"))

result = first_number > second_number or second_number > third_number   # (or) one true

print(f"{first_number} > {second_number} or {second_number} > {third_number} =\t {result}")