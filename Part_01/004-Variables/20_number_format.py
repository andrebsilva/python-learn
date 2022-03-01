number = 1_234.5
result = number + number

print("Float\t\t{}\t\t{}".format(number, result))
print("Float\t\t{0:f}\t{1:f}".format(number, result))
print("Float\t\t{n:.2f}\t\t{r:.2f}".format(n = number, r = result))