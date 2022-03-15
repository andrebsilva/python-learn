def sum_all(*values):
    result = 0
    for v in values: result += v
    return result

print(sum_all())
print(sum_all(10))
print(sum_all(10, 20))
print(sum_all(10, 20, 30, 40))
