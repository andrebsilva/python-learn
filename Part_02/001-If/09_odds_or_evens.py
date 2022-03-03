number = int(input("Number [0 to 100]: "))

print({True: "Evens [Par]", False: "Odds [Ímpar]"}[number % 2 == 0])
