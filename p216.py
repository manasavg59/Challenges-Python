# 216. Write a Python Program to check if a string contains both uppercase and lowercase letters using recursion.
def has_upper_and_lower(text, has_upper=False, has_lower=False):
    if text == "":
        return has_upper and has_lower
    if text[0].isupper():
        has_upper = True
    if text[0].islower():
        has_lower = True
    return has_upper_and_lower(text[1:], has_upper, has_lower)

text = input("Enter a string: ")
if has_upper_and_lower(text):
    print("The string contains both uppercase and lowercase letters")
else:
    print("The string does not contain both uppercase and lowercase letters")