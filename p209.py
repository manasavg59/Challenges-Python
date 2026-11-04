# 209. Write a Python Program to check if a string contains only alphabets using recursion.
def only_alphabets(text):
    if text == "":
        return True
    if not text[0].isalpha():
        return False
    return only_alphabets(text[1:])

text = input("Enter a string: ")
if text != "" and only_alphabets(text):
    print("The string contains only alphabets")
else:
    print("The string does not contain only alphabets")