first_number = int(input("Number 1 [0 to 100]: "))
second_number = int(input("Number 2 [0 to 100]: "))

print({True: "Both are the same", False: {True: f"Bigger {first_number}", False: f"Bigger {second_number}"}[first_number > second_number]}[first_number == second_number])
