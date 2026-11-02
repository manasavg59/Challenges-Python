# 196. Write a Python Program to check if a string contains both uppercase and lowercase letters.
text = input("Enter a string: ")
has_upper = False
has_lower = False
for ch in text:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True

if has_upper and has_lower:
    print("The string contains both uppercase and lowercase letters")
else:
    print("The string does not contain both uppercase and lowercase letters")