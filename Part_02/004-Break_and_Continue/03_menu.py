while True:
    for i in range(1, 10):
        print(f"Option {i} - Run()")
    else:
        print(f"Option 0 - EXIT")
        option = eval(input("[0 to 9]:\t"))
        if option == 0:
            break
        else:
            continue