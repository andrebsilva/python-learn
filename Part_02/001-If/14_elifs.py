year = eval(input("Year of birth: "))

if year < 1945:
    print("War generation")
elif year < 1965:
    print("Baby Boomers")
elif year < 1980:
    print("Generation X")
elif year < 1995:
    print("Generation Y")
else:
    print("Generation Z")