# Task

# You are given two integer arrays,  and  of dimensions X.
# Your task is to perform the following operations:

# Add ( + )
# Subtract ( - )
# Multiply ( * )
# Integer Division ( / )
# Mod ( % )
# Power ( ** )
# Note
# There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

# Input Format

# The first line contains two space separated integers,  and .
# The next  lines contains  space separated integers of array .
# The following  lines contains  space separated integers of array .

# Output Format

# Print the result of each operation in the given order under Task.

import numpy as np


N, M = map(int, input().split())
list1=[]
list2=[]
for _ in range(N):
    line=list(map(int,input().split()))
    list1.append(line)
for _ in range(N):
    line=list(map(int,input().split()))
    list2.append(line)

nparray1=np.array(list1)
nparray2=np.array(list2)
print(nparray1+nparray2)
print(nparray1-nparray2)
print(nparray1*nparray2)
print(nparray1//nparray2)
print(nparray1%nparray2)
print(nparray1**nparray2)
