import network
import time
import urequests
import json

# Wi-Fi credentials
SSID = "JIO_5G"
PASSWORD = "GIRISHB1994"

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    wlan.connect(SSID, PASSWORD)

    timeout = 15
    while not wlan.isconnected() and timeout > 0:
        print(".", end="")
        time.sleep(1)
        timeout -= 1

print()

if wlan.isconnected():
    print("Connected!")
    print("IP:", wlan.ifconfig()[0])
else:
    print("Failed to connect")
    raise SystemExit

# Example location: Bengaluru
LAT = 12.9716
LON = 77.5946

url = (
    "https://api.open-meteo.com/v1/forecast?latitude=12.9716&longitude=77.5946&current_weather=true"
).format(LAT, LON)

try:
    r = urequests.get(url)
    data = r.json()
    r.close()

    print(data["current_weather"])

except Exception as e:
    print("Error:", e)