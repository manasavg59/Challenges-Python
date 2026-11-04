# 207. Write a Python Program to check if a string is pangram using recursion.
def is_pangram(text, letters="abcdefghijklmnopqrstuvwxyz"):
    if letters == "":
        return True
    if letters[0] not in text:
        return False
    return is_pangram(text, letters[1:])

text = input("Enter a string: ").lower()
if is_pangram(text):
    print("The string is a pangram")
else:
    print("The string is not a pangram")