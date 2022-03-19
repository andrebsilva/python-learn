rectangle_area = lambda base, height: base * height

get_base = eval(input('Rectangle base:\t\t'))
get_height = eval(input('Rectangle height:\t'))

print("Rectangle area: ", rectangle_area(get_base, get_height), sep = "\t")