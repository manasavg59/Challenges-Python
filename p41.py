# Program Name: Read a Text File

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()