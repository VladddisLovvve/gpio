import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledTransfer = {0:24, 1:25, 2:8, 3:7, 4:12, 5:16, 6:20, 7:21}

def lightAll():
    for i in range(8):
        ledNumber = ledTransfer[i]
        GPIO.setup(ledNumber, GPIO.OUT)
        GPIO.output(ledNumber, 1)

def lightUp(ledNumber, period, mode = 1):
    ledNumber = ledTransfer[ledNumber]
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, mode)
    time.sleep(period)
    GPIO.output(ledNumber, not mode)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    ledNumber = 0
    for i in range(8*count):
        if ledNumber > 7:
            ledNumber %= 8
        lightUp(ledNumber, period)
        ledNumber += 1

def runningDark(count, period):
    lightAll()
    ledNumber = 0
    for i in range(8*count):
        if ledNumber > 7:
            ledNumber %= 8
        lightUp(ledNumber, period, 0)
        ledNumber += 1

def decToBinList(decNumber):
    binNumber = bin(decNumber)[2:]
    binNumber = [int(x) for x in binNumber]
    i = 8 - len(binNumber)
    binNumber = [0]*i + binNumber
    return binNumber

def lightNumber(number):
    d = list(ledTransfer.values())[::-1]
    d = [d[x] for x in range(len(d)) if decToBinList(number)[x] != 0]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)
    time.sleep(2)
    GPIO.output(d, 0)

# decToBinList[::-1]


    # GPIO.setup(list(ledTransfer.values()), GPIO.OUT)
    # GPIO.output(list(ledTransfer.values()), 1)
    # runningLight(count, period, mode = 0)
    # for x in range(8):
    #     x = ledTransfer[x]
    #     GPIO.setup(x, GPIO.OUT)
    #     GPIO.output(x, 1)
    # time.sleep(period)
    # for x in range(8):
    #     x = ledTransfer[x]
    #     GPIO.setup(x, GPIO.OUT)
    #     GPIO.output(x, 1)


# 2 task

# ledNumber = int(input())
# blinkCount = int(input())
# blinkPeriod = float(input())

# blink(ledNumber, blinkCount, blinkPeriod)

# 3 task

# count = int(input())
# period = float(input())

# runningLight(count, period)

# 4 task

count = 4
period = float(input())

runningDark(count, period)

#5

# decNumber = int(input())

# decToBinList(decNumber)



GPIO.cleanup()
