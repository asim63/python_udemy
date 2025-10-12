import smtplib 

my_email = "dummyperson345@gmail.com"
password = "imab ujjw qpbq idht "

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password= password)
connection.sendmail(from_addr = my_email, to_addrs = "asimdkt64@gmail.com", msg = "Subject:Happy Birthday!!\n\n Happy birthday my g.")
connection.close()