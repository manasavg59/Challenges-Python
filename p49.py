# Program Name: Remove Blank Lines from a File

file = open("sample.txt", "r")

lines = file.readlines()

file.close()

file = open("sample.txt", "w")

for line in lines:

    if line.strip() != "":
        file.write(line)

file.close()

print("Blank lines removed successfully.\n")