# 245. Write a Python Program to calculate covariance of two lists.
x = list(map(float, input("Enter first list (space separated): ").split()))
y = list(map(float, input("Enter second list (space separated): ").split()))

if len(x) != len(y):
    print("Both lists must have the same number of elements")
else:
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    total = 0
    for i in range(n):
        total += (x[i] - mean_x) * (y[i] - mean_y)
    covariance = total / n

    print("Covariance =", covariance)