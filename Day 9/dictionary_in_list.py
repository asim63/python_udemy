travel_log = [
{
    "country" : "France",
    "visits" : 12,
    "cities" :["Paris","Lille","Dijon"]
},
{
    "country" : "Germany",
    "visits" : 5,
    "cities" : ["Berlin","Hamburg","Stuttgart"]
}
]
def add_new_country (new_country,a,b):
    travel_log.append({"country":new_country,
                       "visits": a,
                       "cities": b
                       })
    


add_new_country("Russia",2,["Moscow","Saint Pertersburg"])
print(travel_log)