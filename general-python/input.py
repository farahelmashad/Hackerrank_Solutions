# Task

# You are given a polynomial  of a single indeterminate (or variable), .
# You are also given the values of  and . Your task is to verify if .

x, k=map(int,input().split())
poly=input()
if eval(poly)==k:
    print(True)
else:
    print(False)