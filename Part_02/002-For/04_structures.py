list_numbers    = [1, 2, 3, 4]
for l in list_numbers: print(l, end = '\t')
print()

set_numbers     = {1, 2, 3, 4}
for s in set_numbers: print(s * 2, end = '\t')
print()

tuple_numbers   = (1, 2, 3, 4)
for t in tuple_numbers: print(t * 3, end = '\t')
print()

dict_numbers    = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for dk in dict_numbers.keys(): print(dk, end = '\t')
print()

for dv in dict_numbers.values(): print(dv * 4, end = '\t')
print()

