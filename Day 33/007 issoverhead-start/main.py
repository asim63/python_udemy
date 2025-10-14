import requests
from datetime import datetime
import smtplib

MY_LAT= 27.688123
MY_LONG = 85.375863
MY_EMAIL = "dummyperson345@gmail.com"
password = "imabujjwqpbqidht"

def close_or_not():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LONG + 5 >= iss_longitude >= MY_LONG - 5 :
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def dark_or_not():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "tzid": "Asia/Katmandu",
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise)
    # print(sunset)

    time_now = datetime.now()
    hour = time_now.hour
    # print(hour)
    if hour >= sunset and hour <= sunrise:
        return True
    else:
        return False 
    
# if close_or_not() and dark_or_not():
if True:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = password)
        connection.sendmail(from_addr = MY_EMAIL,
                            to_addrs= "asimdkt64@gmail.com",
                            msg="Subject: LOOK UP FOR ISS\n\nHEY the ISS can be seen in the sky go out and watch the sky."
                            )
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



