first_number = 123
last_number = 456

print(first_number, last_number, sep = " ")
print(first_number * 2, last_number * 2, sep = " ")

print(f"{first_number} {last_number}")
print(f"{first_number * 2} {last_number * 2}")

print("%s %s" %(first_number, last_number))
print("%s %s" %(first_number * 2, last_number * 2))

print("{} {}".format(first_number, last_number))
print("{} {}".format(first_number * 2, last_number * 2))

print("{f} {l}".format(f = first_number, l = last_number))
print("{f} {l}".format(f = first_number * 2, l = last_number * 2))
