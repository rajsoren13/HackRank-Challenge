#Problem:Given the names and grades for each student in a class of N  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
#Nested Lists
if __name__ == '__main__':
    students=[]
    number_Students=int(input())
    for _ in range(number_Students):
        name = input()
        score = float(input())
        students.append([name,score])
    print(students)
    scorecard=[]
   
    for student in students:
        scorecard.append(student[1])
    
    print(scorecard)
    uniquescore=set(scorecard)
    print(uniquescore)
    a=[]
    arr_score=list(uniquescore)
    arr_score.sort()
    print(f"==>{arr_score}")
    low_score=[]
    print(f"second lowest:{arr_score[1]}")
    for name,score in students:
        if score==arr_score[1]:
            low_score.append(name)
    low_score.sort()
    for name in low_score:
        print(name)
