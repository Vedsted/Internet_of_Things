import pycom
from machine import UART
from SI7006A20 import SI7006A20
import time

# Disables the LED heartbeat
#pycom.heartbeat(False)

uart = UART(0)
uart.init(115200, bits=8, parity=None, stop=1)

temp_sensor = SI7006A20()

while True:
    temp = temp_sensor.temperature()
    print(temp)
    time.sleep(1)