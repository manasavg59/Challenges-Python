# 212. Write a Python Program to check if a string contains only lowercase letters using recursion.
def only_lowercase(text):
    if text == "":
        return True
    if not (text[0].isalpha() and text[0].islower()):
        return False
    return only_lowercase(text[1:])

text = input("Enter a string: ")
if text != "" and only_lowercase(text):
    print("The string contains only lowercase letters")
else:
    print("The string does not contain only lowercase letters")