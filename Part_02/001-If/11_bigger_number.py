first_number = int(input("Number 1 [0 to 100]: "))
second_number = int(input("Number 2 [0 to 100]: "))

if first_number == second_number: print("Both are the same")
elif first_number > second_number: print("Bigger: ", first_number)
else: print("Bigger: ", second_number)