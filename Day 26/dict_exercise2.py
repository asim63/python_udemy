weather_c = {
    "Monday" : 12,
    "Tueday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24,
}
print(weather_c)

weather_f = {weather : (9/5*temp + 32) for(weather,temp) in weather_c.items()}

print(weather_f)