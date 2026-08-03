from time import localtime


def format_time(timestamp):
    timestamp += 19800  # IST = UTC +5:30
    t = localtime(timestamp)
    return "{:02d}:{:02d}".format(t[3], t[4])


def get_icon(weather):

    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Fog": "🌫️"
    }

    return icons.get(weather, "🌍")


def get_advice(weather, temp):

    if weather == "Rain":
        return "Carry an Umbrella ☔"

    if temp > 35:
        return "Stay Hydrated 🥤"

    if temp < 18:
        return "Wear a Jacket 🧥"

    return "Have a Great Day 😊"


def generate_dashboard(data):

    icon = get_icon(data["weather"])

    advice = get_advice(
        data["weather"],
        data["temp"]
    )

    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta http-equiv="refresh" content="60">

<title>ESP32 Weather Dashboard</title>

<style>

body{{
background:#0f172a;
color:white;
font-family:Arial;
padding:30px;
}}

.card{{
background:#1e293b;
width:650px;
margin:auto;
padding:20px;
border-radius:12px;
}}

table{{
width:100%;
font-size:20px;
}}

td{{
padding:10px;
}}

</style>

</head>

<body>

<div class="card">

<h1>{icon} Smart Weather Dashboard</h1>

<table>

<tr><td>📍 City</td><td>{data["city"]}, {data["country"]}</td></tr>

<tr><td>🌤 Weather</td><td>{data["description"]}</td></tr>

<tr><td>🌡 Temperature</td><td>{data["temp"]} °C</td></tr>

<tr><td>🤒 Feels Like</td><td>{data["feels"]} °C</td></tr>

<tr><td>💧 Humidity</td><td>{data["humidity"]}%</td></tr>

<tr><td>🌬 Wind</td><td>{data["wind"]} m/s</td></tr>

<tr><td>📈 Pressure</td><td>{data["pressure"]} hPa</td></tr>

<tr><td>👀 Visibility</td><td>{data["visibility"]} km</td></tr>

<tr><td>🌅 Sunrise</td><td>{format_time(data["sunrise"])}</td></tr>

<tr><td>🌇 Sunset</td><td>{format_time(data["sunset"])}</td></tr>

<tr><td>💡 Advice</td><td>{advice}</td></tr>

</table>

</div>

</body>

</html>

"""

    return html