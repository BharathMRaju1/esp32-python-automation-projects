# ESP32 Smart Room Controller

A simple web-based Smart Room Controller built using ESP32-WROOM-32 and MicroPython.

## Features

- Control four virtual rooms
- Individual ON/OFF controls
- ALL ON and ALL OFF buttons
- Built-in web server
- Wi-Fi enabled
- Mobile friendly

## Hardware

- ESP32-WROOM-32
- 4 LEDs (or fewer for testing)
- 220Ω resistors
- Breadboard
- Jumper wires

## Software

- MicroPython
- Thonny IDE

## Project Structure

```
main.py
wifi.py
secrets_example.py
```

## How to Run

1. Flash MicroPython.
2. Copy the files to the ESP32.
3. Rename `secrets_example.py` to `secrets.py`.
4. Enter your Wi-Fi credentials.
5. Run `main.py`.
6. Open the printed IP address in a browser.

## Future Improvements

- Live LED status
- Responsive UI
- Password protection
- AJAX updates
- MQTT support

## License

MIT