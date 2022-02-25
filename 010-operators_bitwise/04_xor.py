first_number = eval(input("Number:\t"))
second_number = eval(input("Number:\t"))

result = first_number ^ second_number   # (^) binary xor

print(f"{first_number}:\t{first_number:08b}")
print(f"{second_number}:\t{second_number:08b}")
print(f"{result}:\t{result:08b}")