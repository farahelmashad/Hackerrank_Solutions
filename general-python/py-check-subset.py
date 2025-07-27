# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .

# If set  is subset of set , print True.
# If set  is not a subset of set , print False.

# Input Format

# The first line will contain the number of test cases, .
# The first line of each test case contains the number of elements in set .
# The second line of each test case contains the space separated elements of set .
# The third line of each test case contains the number of elements in set .
# The fourth line of each test case contains the space separated elements of set .

n=int(input())
for _ in range(n):
    m=int(input())
    a=set(map(int,input().split()))
    l=int(input())
    b=set(map(int,input().split()))
    issubset=True
    if len(a.difference(b))==0:
        print(True)
    else:
        print(False)
