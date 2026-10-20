# 132. Write a Python Program to check if a character is a special symbol.
ch = input("Enter a character: ")
if not ch.isalnum() and not ch.isspace():
    print(ch, "is a special symbol")
else:
    print(ch, "is not a special symbol")