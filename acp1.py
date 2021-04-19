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


def create_value():
    while True:
        value = input()
        if value.isdigit() or (value[0] == "-" and value[1:].isdigit()):
            value = int(value)
        else:
            print("Некорректное значение. Попробуйте ещё раз.")
            continue
        if value == -1:
            return -1
        elif 0 <= value <= 255:
            return value
        else:
            print("Некорректное значение. Попробуйте ещё раз.")
            continue
    

def num2dac(value, sleep_time = 1):
    binNumber = bin(value)[2:]
    binNumber = [int(x) for x in binNumber]
    i = 8 - len(binNumber)
    binNumber = [0]*i + binNumber
    d = list(leds)
    d = [d[x] for x in range(len(d)) if binNumber[x] != 0]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)
    # time.sleep(sleep_time)
    # GPIO.output(d, 0)
    print(value, "=", round(value / 255 * 3.3, 2))


GPIO.setup(leds + [17], GPIO.OUT)
GPIO.output(17, 1)

try:
    while True:
        print("Введите значение от 0 до 255(-1 для выхода): ")
        value = create_value()
        if value == -1:
            exit()
        GPIO.output(leds, [0] * 8)
        num2dac(value)
finally:
    GPIO.cleanup()
