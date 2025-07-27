# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    numbers=list(arr)
    first_max=-1000
    second=-2000
    for i in numbers:
        if i >first_max:
            second=first_max
            first_max=i
        elif i> second  and i != first_max:
            second=i
    print(second)
