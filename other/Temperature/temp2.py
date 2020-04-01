import pycom
from machine import UART
from MPL3115A2 import MPL3115A2
import time

# Disables the LED heartbeat
#pycom.heartbeat(False)

uart = UART(0)
uart.init(115200, bits=8, parity=None, stop=1)

temp_sensor = MPL3115A2()

while True:
    temp = temp_sensor.temperature()
    print(temp)
    time.sleep(1)