import pycom, time
from machine import UART
from builtins import bytes


# Init
pycom.heartbeat(False) # Disable the heartbeat LED
uart = UART(0, 115200)                                  # init with bus=1
uart.init(baudrate=115200, bits=8, parity=None, stop=1)    # init with given parameters



def turnOn(color):
    pycom.rgbled(color)

#def rgbToInt(r, g, b):
#    return int(str(bytes([r, g, b])).replace("b", "").replace("'", "").replace("\\x", ""), 16)

def rgbToInt(r,g,b):
    red = int(bin(r)+'0000000000000000', 2)
    green = int(bin(g)+'00000000', 2)
    return red + green + b

while True:
    # Receive
    received = uart.read(4)
    
    if received != None:
        # Parse
        cmd = received[0]
        r = received[1]
        g = received[2]
        b = received[3]

        if cmd == 0x00:
            print("changeing color")
            turnOn(rgbToInt(r,g,b))
        
