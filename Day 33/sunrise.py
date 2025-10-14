import requests
import datetime as dt

MY_LAT= 27.688123
MY_LNG = 85.375863

parameters = {
    "lng": MY_LNG,
    "lat": MY_LAT,
    "tzid": "Asia/Katmandu",
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json",params = parameters )
response.raise_for_status()
data = response.json()
sunrise = data["results"]['sunrise'].split("T")[1].split(":")[0]
sunset = data["results"]['sunset'].split("T")[1].split(":")[0]

time_now = dt.datetime.now()
print(time_now.hour)
print(sunrise)
print(sunset)
