import smtplib
import datetime as dt
import random
import pandas as pd

now = dt.datetime.now()
today_month = now.month
today_date = now.day

data =pd.read_csv("Day 32/Birthday_wisher/birthdays.csv")
# data =pd.read_csv("birthdays.csv")
#to access the same row or column loc is used
# date = data.loc[data['month'] == month, 'day'].values[0]

### you could do this as well

# today_tuple = (today_month, today_date)
# birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

# # print(today_tuple)
# # print(birthday_dict)

# if today_tuple in birthday_dict:
#     birthday_person = birthday_dict[today_tuple]
#     print(birthday_person)

if today_month in data.month.values:
    date = data.loc[data['month'] == today_month, 'day'].values[0]
    name = data.loc[(data['month'] == today_month) & (data['day'] == date), 'name'].values[0]
    
    if date == today_date:
        chosen_file = f"Day 32/Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
        # chosen_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
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
            