# 214. Write a Python Program to check if a string contains only special characters using recursion.
def only_special(text):
    if text == "":
        return True
    if text[0].isalnum() or text[0].isspace():
        return False
    return only_special(text[1:])

text = input("Enter a string: ")
if text != "" and only_special(text):
    print("The string contains only special characters")
else:
    print("The string does not contain only special characters")