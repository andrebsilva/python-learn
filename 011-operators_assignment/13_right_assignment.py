first_number = eval(input("Number:\t"))
second_number = eval(input("Number:\t"))

print(f"\n{first_number}:\t{first_number:08b}")
print(f"{second_number}:\t{second_number:08b}")

first_number >>= second_number   # (>>=) binary right assignment

print(f"\n{first_number}:\t{first_number:08b}")