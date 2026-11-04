# 208. Write a Python Program to check if a string contains only digits using recursion.
def only_digits(text):
    if text == "":
        return True
    if not text[0].isdigit():
        return False
    return only_digits(text[1:])

text = input("Enter a string: ")
if text != "" and only_digits(text):
    print("The string contains only digits")
else:
    print("The string does not contain only digits")