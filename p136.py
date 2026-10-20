# 136. Write a Python Program to count special characters in a string.
text = input("Enter a string: ")
count = 0
for ch in text:
    if not ch.isalnum() and not ch.isspace():
        count += 1
print("Number of special characters =", count)