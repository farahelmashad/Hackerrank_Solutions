# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    mylist = []
    N = int(input())
    
    for _ in range(N):
        line = input().split()
        op = line[0]
        
        if op == 'insert':
            mylist.insert(int(line[1]), int(line[2]))
        elif op == 'print':
            print(mylist)
        elif op == 'remove':
            mylist.remove(int(line[1]))
        elif op == 'append':
            mylist.append(int(line[1]))
        elif op == 'sort':
            mylist.sort()
        elif op == 'pop':
            mylist.pop()
        elif op == 'reverse':
            mylist.reverse()
