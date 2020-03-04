from LTR329ALS01 import LTR329ALS01
import time

# Light sensor object
ls = LTR329ALS01()

while True:
    t = ls.light()
    print(t)
    time.sleep(1)


# Log output using: screen -L -Logfile light_log.txt /dev/ttyACM0 115200