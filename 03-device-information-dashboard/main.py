from wifi import connect_wifi
import socket
import machine
import gc
import network
import ubinascii
import time

# Connect WiFi
wlan = connect_wifi()

# Store boot time
boot_time = time.time()


def get_html():

    ip = wlan.ifconfig()[0]

    cpu = machine.freq() // 1000000

    ram = gc.mem_free() // 1024

    mac = ubinascii.hexlify(wlan.config('mac'), ':').decode().upper()

    uptime = int(time.time() - boot_time)
    
    rssi = wlan.status('rssi')

    html = f"""
<!DOCTYPE html>
<html>

<head>

<title>ESP32 Dashboard</title>

<style>

body{{
background:#f4f4f4;
font-family:Arial;
padding:30px;
}}

.card{{
width:420px;
margin:auto;
background:white;
padding:20px;
border-radius:12px;
box-shadow:0px 0px 10px gray;
}}

h1{{
text-align:center;
}}

table{{
width:100%;
font-size:18px;
}}

td{{
padding:8px;
}}

</style>

</head>

<body>

<div class="card">

<h1>ESP32 Dashboard</h1>

<table>

<tr>
<td>WiFi Status</td>
<td>Connected</td>
</tr>

<tr>
<td>IP Address</td>
<td>{ip}</td>
</tr>

<tr>
<td>CPU Frequency</td>
<td>{cpu} MHz</td>
</tr>

<tr>
<td>Free RAM</td>
<td>{ram} KB</td>
</tr>

<tr>
<td>MAC Address</td>
<td>{mac}</td>
</tr>

<tr>
<td>Uptime</td>
<td>{uptime} sec</td>
</tr>

<tr>
    <td>Signal Strength</td>
    <td>{rssi} db</td>
</tr>

</table>

</div>

</body>

</html>
"""

    return html


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()

server.bind(addr)

server.listen(1)

print("Server Started")
print("Open:", wlan.ifconfig()[0])

while True:

    client, address = server.accept()

    print("Client Connected:", address)

    request = client.recv(1024)

    response = get_html()

    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html\r\n")
    client.send("Connection: close\r\n\r\n")

    client.sendall(response)

    client.close()