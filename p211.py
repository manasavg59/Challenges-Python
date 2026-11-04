# 211. Write a Python Program to check if a string contains only uppercase letters using recursion.
def only_uppercase(text):
    if text == "":
        return True
    if not (text[0].isalpha() and text[0].isupper()):
        return False
    return only_uppercase(text[1:])

text = input("Enter a string: ")
if text != "" and only_uppercase(text):
    print("The string contains only uppercase letters")
else:
    print("The string does not contain only uppercase letters")