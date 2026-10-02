# Program 74: Reverse a String Using Recursion

def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

s = input("Enter a string: ")

result = reverse_string(s)

print("Reversed string:", result)