first_number = 10
second_number = 12

print("|{:<14}|{:^14}|{:>14}|".format(first_number, second_number, first_number))
print("|{0:<14}|{1:^14}|{0:>14}|".format(first_number, second_number))
print("|{fn:<14}|{sn:^14}|{fn:>14}|".format(fn = first_number, sn = second_number))
