import RPi.GPIO as GPIO
import time

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


GPIO.setmode(GPIO.BCM)

leds = [10, 9, 11, 5, 6, 13, 19, 26][::-1]

try:
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(4, GPIO.IN)
    GPIO.output(17, 1)
    GPIO.setup(leds, GPIO.OUT)
    var_prev = 0
    while True:
        var = simple_acp()
        if var != var_prev:
            var_prev = var 
            print("Digital value:", var, "Analog value:", round(var / 255 * 3.3, 2))
finally:
    GPIO.cleanup()
