from wifi import connect_wifi
from weather import get_weather
from dashboard import generate_dashboard

import socket
import time

# Connect to WiFi
wlan = connect_wifi()

# Create socket
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(1)

print("\n===================================")
print("ESP32 Smart Weather Dashboard")
print("===================================")
print("Open Browser:")
print("http://" + wlan.ifconfig()[0])
print("===================================\n")

weather_cache = None
last_update = 0

while True:

    client, address = server.accept()

    print("Client Connected:", address)

    request = client.recv(1024)

    current = time.time()

    if current - last_update > 60 or weather_cache is None:

        print("Updating weather...")

        weather_cache = get_weather()

        last_update = current

    if weather_cache is None:

        html = """
<html>
<head><title>Error</title></head>
<body style="font-family:Arial;text-align:center;">
<h2>Unable to fetch weather.</h2>
</body>
</html>
"""

    else:

        html = generate_dashboard(weather_cache)

    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html; charset=UTF-8\r\n")
    client.send("Connection: close\r\n\r\n")

    client.send(html)

    client.close()