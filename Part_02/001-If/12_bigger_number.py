first_number = int(input("Number 1 [0 to 100]: "))
second_number = int(input("Number 2 [0 to 100]: "))

print("Both are the same") if first_number == second_number else print("Bigger: ", first_number) if first_number > second_number else print("Bigger: ", second_number)