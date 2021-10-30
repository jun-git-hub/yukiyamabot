import requests
import datetime

API_KEY = 'f29b3ea5029bdb87545aa8fa70d6e298'

def getWeather(LON, LAN):
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall",
        {},
        {
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
        print("-------------------------")
        print(datetime.datetime.fromtimestamp(hour["dt"])) #UNIX時間を日時に変換
        print(hour["weather"][0]["description"]) #天気

    return
