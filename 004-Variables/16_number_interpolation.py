first_number = 123
last_number = 456

print(first_number, last_number, sep = " ")
print(f"{first_number} {last_number}")
print("%s %s" %(first_number, last_number))
print("{} {}".format(first_number, last_number))
print("{0} {1}".format(first_number, last_number))
print("{fn} {ln}".format(fn = first_number, ln = last_number))