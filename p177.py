# 177. Write a Python Program to reverse order of lines in a file.
filename = input("Enter file name: ")
with open(filename, "r") as file:
    lines = file.readlines()

lines.reverse()
print("Lines in reverse order:")
for line in lines:
    print(line, end="")