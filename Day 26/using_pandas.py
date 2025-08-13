student_dict = {
    "student" : ["asim", "bikash", "galij"],
    "score" : [45, 87, 34]
}

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)



# for (key,value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == 'bikash':
        print(row.score)