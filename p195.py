# 195. Write a Python Program to check if a string contains both letters and digits.
text = input("Enter a string: ")
has_letter = False
has_digit = False
for ch in text:
    if ch.isalpha():
        has_letter = True
    if ch.isdigit():
        has_digit = True

if has_letter and has_digit:
    print("The string contains both letters and digits")
else:
    print("The string does not contain both letters and digits")