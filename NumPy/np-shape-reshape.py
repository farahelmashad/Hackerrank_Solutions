# Task

# You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

# Input Format

# A single line of input containing  space separated integers.

# Output Format

# Print the X NumPy array.

import numpy
array=list(map(int,input().split()))
num=numpy.array(array)
print(num.reshape(3,3))

