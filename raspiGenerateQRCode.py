from escpos import *
from time import sleep
import RPi.GPIO as GPIO

print('start')
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

a = 'A'
no = 0

while True:
    if GPIO.input(26):
        sleep(1)
        no = no + 1
        myS = a + str(no)
        print(myS)

        if no == 100:
            no = 0

        p = printer.File("/dev/usb/lp0")
        p.set(align="CENTER")
        p.qr(myS, size=8, native=True)
        p.text("\n\n\n")
        p.cut()
        p.close()

GPIO.cleanup()
