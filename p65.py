# Program Name: Function to Return the Reverse of a String

def reverse_string(text):
    return text[::-1]


text = input("Enter a string: ")

print("Reversed string:", reverse_string(text))