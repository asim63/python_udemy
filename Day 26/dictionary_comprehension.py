# new_dict = {new_key:new_value for item in list}

# new_dict - {new_key:new_value for (key,value) in dict.items() if test}
import random
names = ['Alex','Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']


student_score = {
    student : random.randint(1,100) for student in names
} 
print(student_score)
passed_students = {
    student : marks for (student, marks) in student_score.items() if marks>= 60}
print(passed_students)

