import RPi.GPIO as GPIO
from time import sleep
import time
import vlc

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.IN)

tSleep = 10;
i = 0
d = 0.00
arrUS = [0.00]*3

media_player = vlc.MediaPlayer()
media_player.set_fullscreen(True)

media = vlc.Media("/home/pi/v1.mp4")
media_player.set_media(media)

def readUS():
    GPIO.output(13, True)
    sleep(0.00001)
    GPIO.output(13, False)
    while GPIO.input(19) == 0:
        pass
    start = time.time()
    while GPIO.input(19) == 1:
        pass
    end = time.time()
    d = (end - start) * 34300 / 2
    print(d)

while True:
    readUS()

    arrUS[i] = d
    if arrUS[0] == arrUS [1] == arrUS[2]:
        media_player.play()
        sleep(tSleep)
        media_player.stop()

    i = i + 1
    if i == 3:
        i = 0

    print(arrUS, d, i)
    sleep(1)
