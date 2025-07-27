# Task

# You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

# Input Format

# The first line contains space separated integers ,  and .
# The next  lines contains the space separated elements of the  columns.
# After that, the next  lines contains the space separated elements of the  columns.

# Output Format

# Print the concatenated array of size X.
import numpy as np

N, M ,P= map(int, input().split())
list1=[]
list2=[]
for _ in range(N):
    line=list(map(int,input().split()))
    list1.append(line)
for _ in range(M):
    line=list(map(int,input().split()))
    list2.append(line)
nparray1=np.array(list1)
nparray2=np.array(list2)
concatenated=np.concatenate((nparray1,nparray2), axis=0)
print(concatenated)
