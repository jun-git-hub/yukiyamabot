import requests
import datetime

API_KEY = 'f29b3ea5029bdb87545aa8fa70d6e298'

def getWeather(LON, LAN):
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall",
        headers={},
        params={
        "appid":API_KEY,
        "lon":LON,
        "lat":LAN,
        "units":"metric",
        "lang":"ja",
        "exculde":"current,minutely,daily,alerts"
        }
    )
    jsondata = data.json()
    
    for hour in jsondata["hourly"]:
        print("-------------------------/n")
        print(datetime.datetime.fromtimestamp(hour["dt"])
        print(hour["weather"][0]["description"])
        
    return weather