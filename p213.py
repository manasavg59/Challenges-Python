# 213. Write a Python Program to check if a string contains only whitespace using recursion.
def only_whitespace(text):
    if text == "":
        return True
    if not text[0].isspace():
        return False
    return only_whitespace(text[1:])

text = input("Enter a string: ")
if text != "" and only_whitespace(text):
    print("The string contains only whitespace")
else:
    print("The string does not contain only whitespace")