# 📡 WiFi Scanner

A web-based WiFi Scanner built using **ESP32-WROOM-32** and **MicroPython**. This project scans nearby wireless networks and displays their information through a browser-based dashboard.

## ✨ Features

- 📶 Scan nearby WiFi networks
- 📊 Display Signal Strength (RSSI)
- 🔒 Show Security Type
- 📡 Display WiFi Channel
- 🔄 Refresh scan from the web interface
- 🌐 Accessible from any device on the same network

## 🛠 Hardware

- ESP32-WROOM-32

## 💻 Software

- MicroPython
- Thonny IDE
- Python

## 📂 Project Structure

```
main.py
wifi.py
secrets_example.py
README.md
```

## 🚀 How to Run

1. Flash MicroPython on the ESP32.
2. Upload all project files.
3. Rename `secrets_example.py` to `secrets.py`.
4. Add your WiFi credentials.
5. Run `main.py`.
6. Open the IP address displayed in the Thonny console.

## 📚 Concepts Learned

- WiFi Network Scanning
- Socket Programming
- Dynamic HTML Generation
- RSSI (Signal Strength)
- Authentication Modes
- Sorting Data in Python

## 🚀 Future Improvements

- Auto Refresh every 5 seconds
- Display Hidden Networks
- Show BSSID (MAC Address)
- Export Scan Results to CSV
- Search and Filter Networks
- Dark Mode UI

## 👨‍💻 Author

Bharath M
