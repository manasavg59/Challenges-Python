# 244. Write a Python Program to calculate correlation coefficient of two lists.
import math

x = list(map(float, input("Enter first list (space separated): ").split()))
y = list(map(float, input("Enter second list (space separated): ").split()))

if len(x) != len(y):
    print("Both lists must have the same number of elements")
else:
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    covariance = 0
    var_x = 0
    var_y = 0
    for i in range(n):
        covariance += (x[i] - mean_x) * (y[i] - mean_y)
        var_x += (x[i] - mean_x) ** 2
        var_y += (y[i] - mean_y) ** 2

    correlation = covariance / math.sqrt(var_x * var_y)
    print("Correlation coefficient =", correlation)