# Program Name: Function to Calculate Power Using Recursion

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Result:", power(base, exponent))