# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

def count_substring(string, sub_string):
    window=len(sub_string)
    count=0
    for i in range(len(string)-window+1):
        if string[i:i+window]==sub_string:
            count+=1
        
    return count
