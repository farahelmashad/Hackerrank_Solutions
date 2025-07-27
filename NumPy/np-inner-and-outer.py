# Task

# You are given two arrays:  and .
# Your task is to compute their inner and outer product.

# Input Format

# The first line contains the space separated elements of array .
# The second line contains the space separated elements of array .

# Output Format

# First, print the inner product.
# Second, print the outer product.

import numpy

array1=numpy.array(list(map(int,input().split())))
array2=numpy.array(list(map(int,input().split())))
print(numpy.inner(array1,array2))
print(numpy.outer(array1,array2))
