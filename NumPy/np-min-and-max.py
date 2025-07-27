# Task

# You are given a 2-D array with dimensions X.
# Your task is to perform the min function over axis  and then find the max of that.

# Input Format

# The first line of input contains the space separated values of  and .
# The next  lines contains  space separated integers.

# Output Format

# Compute the min along axis  and then print the max of that result.

import numpy

N, M = map(int, input().split())
list1=[]
for _ in range(N):
    line=list(map(int,input().split()))
    list1.append(line)
nparray=numpy.array(list1)
min_array=nparray.min(axis=1)
print(min_array.max())
