# 210. Write a Python Program to check if a string contains only alphanumeric characters using recursion.
def only_alphanumeric(text):
    if text == "":
        return True
    if not text[0].isalnum():
        return False
    return only_alphanumeric(text[1:])

text = input("Enter a string: ")
if text != "" and only_alphanumeric(text):
    print("The string contains only alphanumeric characters")
else:
    print("The string does not contain only alphanumeric characters")