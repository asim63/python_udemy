##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import datetime as dt
import random
import pandas as pd

file1 = r"Day 32\Birthday_Wisher\letter_templates\letter_1.txt"
file2 = r"Day 32\Birthday_Wisher\letter_templates\letter_2.txt"
file3 = r"Day 32\Birthday_Wisher\letter_templates\letter_3.txt"
file_list= [file1, file2, file3]
now = dt.datetime.now()
today_month = now.month
today_date = now.day
data = pd.read_csv(r"Day 32\Birthday_Wisher\birthdays.csv")

# print(name_list)
# month = data.month.values[0]

#to access the same row or column loc is used
# date = data.loc[data['month'] == month, 'day'].values[0]

# print(month)
# print(date)
if today_month in data.month.values:
    date = data.loc[data['month'] == today_month, 'day'].values[0]
    name = data.loc[(data['month'] == today_month) & (data['day'] == date), 'name'].values[0]
    
    if date == today_date:
        chosen_file = random.choice(file_list)
        with open(chosen_file, mode ='r') as file:
            content = file.read()
            message = content.replace("[NAME]",name)
            # print(message)
            
            my_email = "dummyperson345@gmail.com"
            password = "imab ujjw qpbq idht "
            birthday_email = data.loc[data['name']== name, 'email'].values[0]
            # print(birthday_email)
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(from_addr= my_email,
                                to_addrs= birthday_email,
                                msg = f"Subject:Happy Birthday\n\n{message}"
                                )
            