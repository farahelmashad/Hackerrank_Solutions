# Task

# You are given two arrays  and . Both have dimensions of X.
# Your task is to compute their matrix product.

# Input Format

# The first line contains the integer .
# The next  lines contains  space separated integers of array .
# The following  lines contains  space separated integers of array .

# Output Format

# Print the matrix multiplication of  and .

import numpy


N=int(input())
list1=[]
list2=[]
for _ in range(N):
    line=list(map(int,input().split()))
    list1.append(line)

for _ in range(N):
    line=list(map(int,input().split()))
    list2.append(line)

nparray=numpy.array(list1)
nparray2=numpy.array(list2)

print(numpy.dot(nparray,nparray2))
