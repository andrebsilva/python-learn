'''
    Built-In Function: format()
    Returns a formatted representation of the given value controlled by the format specifier.
    
    [[fill]align][sign][#][0][width][,][.precision][type]
    where, the options are
    fill        ::=  any character
    align       ::=  "<" | ">" | "=" | "^"
    sign        ::=  "+" | "-" | " "
    width       ::=  integer
    precision   ::=  integer
    type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
'''

print(format(125, 'd'))     # decimal
print(format(125, 'n'))     # number
print(format(125, 'b'))     # binary
print(format(125, 'e'))     # notation
print(format(125, 'E'))     # NOTATION
print(format(125, '-f'))     # float
print(format(125, '.2f'))   # float
print(format(125, 'F'))     # FLOAT
print(format(125, '.3F'))   # FLOAT
print(format(125, 'o'))     # oct
print(format(125, 'x'))     # hex
print(format(125, 'X'))     # HEX
print(format(125, 'c'))     # character
print(format('125', 's'))   # string
print(format(125, '%'))     # percent
