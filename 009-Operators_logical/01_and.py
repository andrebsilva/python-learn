first_number = eval(input("Number:\t"))
second_number = eval(input("Number:\t"))
third_number = eval(input("Number:\t"))

result = first_number > second_number and second_number > third_number # (and) both true

print(f"{first_number} > {second_number} and {second_number} > {third_number}\t= {result}")