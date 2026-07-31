# Buzzer Alarm with Snooze (ESP32 + MicroPython)

An alarm system that rings a buzzer for a set duration, with a button to snooze.

## Hardware
- ESP32 dev board
- Active buzzer (GPIO 25)
- Push button / onboard BOOT button (GPIO 0)

## How it works
- On boot, waits 5 seconds then starts beeping
- Pressing the button snoozes the alarm for 5 seconds
- Alarm auto-stops after 10 seconds if not interacted with

## How to run
1. Flash MicroPython on the ESP32
2. Upload `main.py` via Thonny
3. Reset the board — alarm starts automatically

## Demo
(add a photo/gif here later)
