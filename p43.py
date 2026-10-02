# Program Name: Count Words in a File

file = open("sample.txt", "r")

content = file.read()

words = content.split()

print("Number of words:", len(words))

file.close()
print("\n")