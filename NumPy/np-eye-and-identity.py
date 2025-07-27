# Task

# Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

# Note

# In order to get alignment correct, please insert the line  below the numpy import.

# Input Format

# A single line containing the space separated values of  and .
#  denotes the rows.
#  denotes the columns.

# Output Format

# Print the desired X array.

import numpy
numpy.set_printoptions(legacy='1.13')

N,M=map(int, input().split())
print(numpy.eye(N,M))
