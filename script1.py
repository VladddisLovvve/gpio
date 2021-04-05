import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledTransfer = {0:10, 1:9, 2:11, 3:5, 4:6, 5:13, 6:19, 7:26}

def num2dac(value):
    binNumber = bin(value)[2:]
    binNumber = [int(x) for x in binNumber]
    i = 8 - len(binNumber)
    binNumber = [0]*i + binNumber
    d = list(ledTransfer.values())[::-1]
    d = [d[x] for x in range(len(d)) if binNumber[x] != 0]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)

try:
    while True:
        print("Write a number (-1 for exit):")
        value = int(input())
        for i in range(8):
            number = ledTransfer[i]
            GPIO.setup(number, GPIO.OUT)
            GPIO.output(number, 0)
        if value == -1:
            break
        else:
            num2dac(value)
finally:
    GPIO.cleanup()

