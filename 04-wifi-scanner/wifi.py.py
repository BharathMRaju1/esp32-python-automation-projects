import network
import time
from secrets import SSID, PASSWORD


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)

        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")

    print("\nConnected!")
    print("IP Address:", wlan.ifconfig()[0])

    return wlan