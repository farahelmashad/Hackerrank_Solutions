# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example

# Print the string .

# Input Format

# The first line contains an integer .
if __name__ == '__main__':
    n = int(input())
    word=""
    for i in range(n):
        word+=str(i+1)
    print(word)
