import datetime as dt

now = dt.datetime.now()
year = now.year
weekday = now.weekday()
print(weekday)
# print(type(now))
# print(type(year))
# print(now)
# print(year)
# if year == 2025:
    # print("yes its 2025")

date_of_birth = dt.datetime(year = 2006, month= 5, day= 8, hour = 10, minute= 9,second = 35)
print(date_of_birth)