from wifi import connect_wifi
import network
import socket

# Connect to WiFi
wlan = connect_wifi()

def security_name(auth):
    security = {
        0: "OPEN",
        1: "WEP",
        2: "WPA-PSK",
        3: "WPA2-PSK",
        4: "WPA/WPA2-PSK"
    }
    return security.get(auth, "Unknown")

def scan_wifi():

    networks = wlan.scan()

    # Sort by strongest signal
    networks.sort(key=lambda x: x[3], reverse=True)

    rows = ""

    for net in networks:

        ssid = net[0].decode('utf-8')

        rssi = net[3]

        auth = security_name(net[4])

        rows += f"""
        <tr>
            <td>{ssid}</td>
            <td>{rssi} dBm</td>
            <td>{auth}</td>
        </tr>
        """

    html = f"""
<!DOCTYPE html>

<html>

<head>

<title>ESP32 WiFi Scanner</title>

<style>

body{{
font-family:Arial;
background:#f2f2f2;
padding:20px;
}}

table{{
width:80%;
margin:auto;
border-collapse:collapse;
background:white;
}}

th,td{{
border:1px solid gray;
padding:10px;
text-align:center;
}}

th{{
background:#2196F3;
color:white;
}}

h1{{
text-align:center;
}}

button{{
padding:10px 20px;
font-size:16px;
margin:20px;
}}

</style>

</head>

<body>

<h1>ESP32 WiFi Scanner</h1>

<center>
<a href="/">
<button>Refresh Scan</button>
</a>
</center>

<table>

<tr>

<th>SSID</th>
<th>RSSI</th>
<th>Security</th>

</tr>

{rows}

</table>

</body>

</html>
"""

    return html


addr = socket.getaddrinfo("0.0.0.0",80)[0][-1]

server = socket.socket()

server.bind(addr)

server.listen(1)

print("Server Started")

print("Open:", wlan.ifconfig()[0])

while True:

    client,address = server.accept()

    request = client.recv(1024)

    response = scan_wifi()

    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type:text/html\r\n")
    client.send("Connection:close\r\n\r\n")

    client.sendall(response)

    client.close()