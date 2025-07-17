# In Python, a string can be split on a delimiter.

def split_and_join(line):
    word=line.split()
    i="-".join(word)
    return i

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
