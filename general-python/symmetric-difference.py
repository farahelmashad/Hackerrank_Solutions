# Task
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
inter=a.intersection(b)
unio=a.union(b)
newset=set(sorted(unio.difference(inter)))
for x in newset:
    print(x)
