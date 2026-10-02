# Program Name: Count Lines in a File

file = open("sample.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()
print("\n")