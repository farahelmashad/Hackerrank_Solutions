# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    scores=sorted(set([s[1] for s in students]))
    second=scores[1]
    student=[s[0] for s in students if s[1]==second  ]
    student.sort()
    for i in student:
        print(i)
     