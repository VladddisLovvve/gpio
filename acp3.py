import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [10, 9, 11, 5, 6, 13, 19, 26][::-1]


def decToBinList(decNumber):
    binNumber = bin(decNumber)[2:]
    binNumber = [int(x) for x in binNumber]
    i = 8 - len(binNumber)
    binNumber = [0]*i + binNumber
    return binNumber



def simple_acp():
    for i in range(256):
        for j in range(8):
            GPIO.output(leds[j], decToBinList(i)[j])
        time.sleep(0.005)
        if GPIO.input(4) == 0:
            break
    return i

def num2dac(value, sleep_time = 10):
    binNumber = bin(value)[2:]
    binNumber = [int(x) for x in binNumber]
    i = 8 - len(binNumber)
    binNumber = [0]*i + binNumber
    leds = [leds[x] for x in range(len(leds)) if binNumber[x] != 0]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)
    tm.sleep(sleep_time)
    GPIO.output(d, 0)


try:
    left, right = 1, 255
    while right-left > 1:
        var = (right + left)//2
        num2dac(var)
        if (right - light > 1) and (GPIO.input(4) == 0):
            right = var
        elif (right - left > 1) and (GPIO.input(4) == 1):
            left = var
        if right - left <= 1:
            print('U =', str((l/255)*3.3)[0:4],'V')
            break

finally:
    GPIO.cleanup()
