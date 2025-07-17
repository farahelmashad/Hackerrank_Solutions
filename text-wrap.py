# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to
# Returns

# string: a single string with newline characters ('\n') where the breaks should be
import math
def wrap(string, max_width):
    length=math.ceil(len(string)/max_width)
    word=""
    for i in range(0,len(string),max_width):
        word+=(string[i:i+max_width]+'\n')
        
    
    return word

