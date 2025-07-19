student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
print(student_scores)
student_grade = {}
for i in student_scores:
    if (student_scores[i]>= 91):
        student_grade[i] = "Outstanding"
    elif (student_scores[i]>= 81):
        student_grade[i] = "Exceeds Expectation"
    elif (student_scores[i]>= 71):
        student_grade[i] = "Acceptable"
    else:
        student_grade[i] = "Fail"

print(student_grade)