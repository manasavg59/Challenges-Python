# 220. Write a Python Program to check if a string contains all vowels using recursion.
def has_all_vowels(text, vowels="aeiou"):
    if vowels == "":
        return True
    if vowels[0] not in text:
        return False
    return has_all_vowels(text, vowels[1:])

text = input("Enter a string: ").lower()
if has_all_vowels(text):
    print("The string contains all vowels")
else:
    print("The string does not contain all vowels")