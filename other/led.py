import pycom

pycom.heartbeat(False)


def turn_on_led(color):
    pycom.rgbled(color)

def turn_off_led():
    pycom.rgbled(0x0) # 0x0 equals to black or turned off

def rgbToInt(red, green, blue):
    red = int(bin(red) + "0000000000000000", 2)
    green = int(bin(green)+"00000000", 2)
    return red + green + blue


while True:
    ## Dummy init: check LEDs are working
    for green in range(0, 255):
        turn_on_led(rgbToInt(255, green, 0))
    for red in reversed(range(0, 255)):
        turn_on_led(rgbToInt(red, 255, 0))
    for blue in range(0, 255):
        turn_on_led(rgbToInt(0, 255, blue))
    for green in reversed(range(0, 255)):
        turn_on_led(rgbToInt(0, green, 255))
    for red in range(0, 255):
        turn_on_led(rgbToInt(red, 0, 255))
    for blue in reversed(range(0, 255)):
        turn_on_led(rgbToInt(255, 0, blue))
