import RPi.GPIO as GPIO
import time 

def num2dac(value):
    binNumber = bin(value)[2:]
    binNumber = [int(x) for x in binNumber]
    i = 8 - len(binNumber)
    binNumber = [0]*i + binNumber
    d = list(ledTransfer.values())[::-1]
    d = [d[x] for x in range(len(d)) if binNumber[x] != 0]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)
    time.sleep(0.1)
    GPIO.output(d, 0)

def turn_off(ledTransfer):
    for i in range(8):
        number = ledTransfer[i]
        GPIO.setup(number, GPIO.OUT)
        GPIO.output(number, 0)

GPIO.setmode(GPIO.BCM)

ledTransfer = {0:24, 1:25, 2:8, 3:7, 4:12, 5:16, 6:20, 7:21}

try:
    print("Enter number of repetitions")
    repetitionsNumber = int(input())
    for num in range(repetitionsNumber):
        for x in range(256):
            num2dac(x)
            turn_off(ledTransfer)
        for x in range(256, -1, -1):
            num2dac(x)
            turn_off(ledTransfer)
finally:
    GPIO.cleanup()