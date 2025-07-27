# Task

# You are given a square matrix  with dimensions X. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

# Input Format

# The first line contains the integer .
# The next  lines contains the  space separated elements of array .

# Output Format

# Print the determinant of .

import numpy

N=int(input())
list1=[]
for _ in range(N):
    line=list(map(float,input().split()))
    list1.append(line)
nparray=numpy.array(list1)
det=numpy.linalg.det(nparray)
print(round(det,2))
