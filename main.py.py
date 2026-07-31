from machine import Pin
import socket
from wifi import connect_wifi

connect_wifi()

led1 = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(5, Pin.OUT)
led4 = Pin(18, Pin.OUT)

html = """
<!DOCTYPE html>
<html>
<head>
<title>ESP32 Smart Controller</title>
<style>
body{
font-family:Arial;
background:#f5f5f5;
text-align:center;
}
button{
width:120px;
height:40px;
margin:10px;
font-size:18px;
}
</style>
</head>

<body>

<h1>ESP32 Smart Room Controller</h1>

<p>Room 1</p>
<a href="/led1/on"><button>ON</button></a>
<a href="/led1/off"><button>OFF</button></a>

<p>Room 2</p>
<a href="/led2/on"><button>ON</button></a>
<a href="/led2/off"><button>OFF</button></a>

<p>Room 3</p>
<a href="/led3/on"><button>ON</button></a>
<a href="/led3/off"><button>OFF</button></a>

<p>Room 4</p>
<a href="/led4/on"><button>ON</button></a>
<a href="/led4/off"><button>OFF</button></a>

<hr>

<a href="/allon"><button>ALL ON</button></a>
<a href="/alloff"><button>ALL OFF</button></a>

</body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(5)

print("Server Started")

while True:

    client, address = server.accept()

    request = client.recv(1024).decode()

    print(request)

    if "/led1/on" in request:
        led1.on()

    elif "/led1/off" in request:
        led1.off()

    elif "/led2/on" in request:
        led2.on()

    elif "/led2/off" in request:
        led2.off()

    elif "/led3/on" in request:
        led3.on()

    elif "/led3/off" in request:
        led3.off()

    elif "/led4/on" in request:
        led4.on()

    elif "/led4/off" in request:
        led4.off()

    elif "/allon" in request:
        led1.on()
        led2.on()
        led3.on()
        led4.on()

    elif "/alloff" in request:
        led1.off()
        led2.off()
        led3.off()
        led4.off()

    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html\r\n")
    client.send("Connection: close\r\n\r\n")
    client.sendall(html)
    client.close()