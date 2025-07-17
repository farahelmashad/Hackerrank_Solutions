# Task

# You have a non-empty set , and you have to execute  commands given in  lines.

# The commands will be pop, remove and discard.

n = int(input()) 
myset = set(map(int,input().split())) 
N = int(input()) 
arr = [] 
for i in range(N): 
  command = list(input().split()) 
  if command[0] == 'pop': 
    myset.discard(min(myset)) 
  else: 
        myset.discard(int(command[1])) 
print(sum(myset))