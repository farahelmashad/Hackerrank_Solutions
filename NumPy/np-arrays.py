# Task

# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.

# Input Format

# A single line of input containing space separated numbers.

# Output Format

# Print the reverse NumPy array with type float.

import numpy

def arrays(arr):
    rev=numpy.array(arr[::-1])
    return rev.astype(float)
