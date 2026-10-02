# Program Name: Function to Find Maximum of Three Numbers

def maximum(a, b, c):

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum:", maximum(a, b, c))




print("\n")