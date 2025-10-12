import smtplib
import datetime as dt
import random

my_email = "dummyperson345@gmail.com"
password = "imab ujjw qpbq idht"
today= dt.datetime.now()
weekday = today.weekday()
# print(weekday)
with open(r"Day 32\Birthday Wisher (Day 32) start\quotes.txt",mode = "r") as file:
    quote_list = file.readlines()
    # print(quote_list)

message = random.choice(quote_list)
# print(message)
if weekday == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(from_addr = my_email,
                            to_addrs= "asimdkt64@gmail.com",
                            msg = f"Subject: Motivation for you!!\n\n{message}")