number = eval(input("Number between 1 and 100: "))

print({True: "Evens", False: "Odds"}[number % 2 == 0])
