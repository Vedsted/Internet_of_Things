import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

while True:
    
    #ser.write(b'\x00\xff\x00\x00')
    #ser.write(bytearray([0, 255, 0, 0]))
    ser.write(bytes([0, 255, 0, 0]))

    time.sleep(0.05)

    #ser.write(b'\x00\x00\x00\xff')
    #ser.write(bytearray([0, 0, 0, 255]))
    ser.write(bytes([0, 0, 0, 255]))
    
    time.sleep(0.05)
