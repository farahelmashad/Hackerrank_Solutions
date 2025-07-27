# Task

# You are given the coefficients of a polynomial .
# Your task is to find the value of  at point .

# Input Format

# The first line contains the space separated value of the coefficients in .
# The second line contains the value of .

# Output Format

# Print the desired value.

import numpy

list1 = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(list1, x))
