'''
    Built-In Function: eval()
    Parses the expression passed to this method and runs python expression (code) within the program.
'''

text = "True"

text_to_eval = eval(text)

print(type(text))
print(type(text_to_eval))