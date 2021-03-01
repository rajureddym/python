def print_sum(student_marks,query_name):
    total = 0
    for key,value in student_marks.items():
        if key == query_name:
            total = sum(value)/len(value)
            print(total)


if __name__ == '__main__':

#read number of students, followed by each student name along with their marks
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

#print given student average marks 
    print_sum(student_marks,query_name)

