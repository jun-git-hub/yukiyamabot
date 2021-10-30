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
    weather = []
    for hour in jsondata["hourly"]:
        weather.append("-------------------------" + "\n" + str(datetime.datetime.fromtimestamp(hour["dt"])) + "\n" + hour["weather"][0]["description"])
    reslt = '\n'.join(weather)
    return reslt