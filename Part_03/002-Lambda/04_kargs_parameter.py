sum_all = lambda **args: sum(args.values())

print(sum_all(first = 2, second = 4, third = 6, fourth = 8))
print(sum_all(**{"first": 2, "second": 4, "third": 6, "fourth": 8}))
print(sum_all(**{"first": 2, "second": 4, "third": 6}, **{"fourth": 8}))