# ejercicio_38.py
import time

hours = 0
minutes = 0
seconds = 0

while True:
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1

