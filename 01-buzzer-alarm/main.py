from machine import Pin
import time

# --- Pin setup ---
buzzer = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)   # button pulls LOW when pressed

# --- Config ---
ALARM_DURATION = 10      # seconds the buzzer rings if not snoozed
SNOOZE_DURATION = 5      # seconds to wait after snooze before ringing again
BEEP_ON = 0.3             # buzzer on-time per beep
BEEP_OFF = 0.2            # buzzer off-time per beep

def ring_alarm():
    print("ALARM! Press the button to snooze.")
    start_time = time.time()

    while time.time() - start_time < ALARM_DURATION:
        # Check if button pressed (LOW because of pull-up)
        if button.value() == 0:
            print("Snoozed!")
            buzzer.value(0)
            time.sleep(SNOOZE_DURATION)
            print("Snooze over. Ringing again...")
            start_time = time.time()   # reset timer after snooze
            continue

        # Beep pattern
        buzzer.value(1)
        time.sleep(BEEP_ON)
        buzzer.value(0)
        time.sleep(BEEP_OFF)

    print("Alarm finished.")

# --- Main loop ---
print("System ready. Alarm will trigger in 5 seconds...")
time.sleep(5)
ring_alarm()
