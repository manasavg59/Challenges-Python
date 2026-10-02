# Program 79: Find Length of a String Using Recursion

def string_length(s):
    if s == "":
        return 0

    return 1 + string_length(s[1:])

s = input("Enter a string: ")

result = string_length(s)

print("Length of string:", result)