# Task

# You are given a X integer array matrix with space separated elements ( = rows and  = columns).
# Your task is to print the transpose and flatten results.

# Input Format

# The first line contains the space separated values of  and .
# The next  lines contains the space separated elements of  columns.

# Output Format

# First, print the transpose array and then print the flatten.

import numpy
N,M=int(input().split())

array=numpy.array(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        array[i][j]=int(input())
        
array.reshape(int(N),int(M))
print(numpy.transpose(array))
print(array.flatten())

