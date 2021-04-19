import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

a = [10, 9, 11, 5, 6, 13, 19, 26]


GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.output(17, 1)


def num2dac(decNumber):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in a:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, 0)
    for i in range(8):
        if decNumber%2 == 0:
            decNumber = decNumber//2
        else:
            b[i] = 1
            decNumber = decNumber//2
    for i in range(8):
        if b[i] == 1:
            GPIO.setup(a[i], GPIO.OUT)
            GPIO.output(a[i], 1)
    time.sleep(0.001)

try:
    l = 1
    r = 255
    while r-l>1:
        m = (r+l)//2
        num2dac(m)
        if (r - l > 1) and (GPIO.input(4) == 0):
            r = m
        elif (r - l > 1) and (GPIO.input(4) == 1):
            l = m
        if r-l<=1:
            print('U =', str((l/255)*3.3)[0:4],'V')
            break
finally:
    GPIO.cleanup()
