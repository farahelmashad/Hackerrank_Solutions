# Task

# You are given a 2-D array of size X.
# Your task is to find:

# The mean along axis 
# The var along axis 
# The std along axis 
# Input Format

# The first line contains the space separated values of  and .
# The next  lines contains  space separated integers.

# Output Format

# First, print the mean.
# Second, print the var.
# Third, print the std.

import numpy

N, M = map(int, input().split())
list1=[]
for _ in range(N):
    line=list(map(int,input().split()))
    list1.append(line)
nparray=numpy.array(list1)

print(nparray.mean(axis=1))
print(nparray.var(axis=0))
print(round(nparray.std(), 11))
