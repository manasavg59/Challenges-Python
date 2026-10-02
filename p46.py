# Program Name: Check Whether a File Exists

import os

filename = input("Enter file name: ")

if os.path.exists(filename):
    print("File exists.\n")
else:
    print("File does not exist.\n")