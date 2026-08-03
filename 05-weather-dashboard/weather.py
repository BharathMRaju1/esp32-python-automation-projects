import urequests
from secrets import API_KEY, CITY

URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():

    url = "{}?q={}&appid={}&units=metric".format(
        URL,
        CITY,
        API_KEY
    )

    print("Connecting to Weather API...")
    print(url)

    try:

        response = urequests.get(url)

        print("HTTP Status:", response.status_code)

        if response.status_code != 200:
            response.close()
            return None

        data = response.json()

        response.close()

        weather = {}

        weather["city"] = data["name"]
        weather["country"] = data["sys"]["country"]

        weather["temp"] = data["main"]["temp"]
        weather["humidity"] = data["main"]["humidity"]
        weather["pressure"] = data["main"]["pressure"]

        weather["feels"] = data["main"]["feels_like"]

        weather["weather"] = data["weather"][0]["main"]

        weather["description"] = data["weather"][0]["description"]

        weather["wind"] = data["wind"]["speed"]

        weather["visibility"] = data.get("visibility", 0) / 1000

        weather["sunrise"] = data["sys"]["sunrise"]

        weather["sunset"] = data["sys"]["sunset"]

        return weather

    except Exception as e:

        print("Weather Error")

        print(e)

        return None