import pycom
import time

pycom.heartbeat(False) # Disable the heartbeat LED

WHITE = 0xFFFFFF
BLACK = 0x000000

def blink(color):
    pycom.rgbled(color)


while True:
    blink(WHITE)
    time.sleep(0.05)
    blink(BLACK)
    time.sleep(0.05)