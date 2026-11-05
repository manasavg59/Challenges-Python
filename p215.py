# 215. Write a Python Program to check if a string contains both letters and digits using recursion.
def has_letters_and_digits(text, has_letter=False, has_digit=False):
    if text == "":
        return has_letter and has_digit
    if text[0].isalpha():
        has_letter = True
    if text[0].isdigit():
        has_digit = True
    return has_letters_and_digits(text[1:], has_letter, has_digit)

text = input("Enter a string: ")
if has_letters_and_digits(text):
    print("The string contains both letters and digits")
else:
    print("The string does not contain both letters and digits")