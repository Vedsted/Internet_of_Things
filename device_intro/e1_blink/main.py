import pycom
import time

pycom.heartbeat(False) # Disable the heartbeat LED

BLUE = 0x0000FF
RED = 0xFF0000
BLACK = 0x000000

def blink(color, duration):
    pycom.rgbled(color)
    time.sleep(1)
    

if __name__ == "__main__":
    for i in range(1, 10):
        blink(RED, 1)
        blink(BLACK, 1)

