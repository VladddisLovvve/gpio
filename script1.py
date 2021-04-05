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
        if value == -1:
            break
        else:
            num2dac(value)
finally:
    GPIO.cleanup()











# import RPi.GPIO as GPIO
# import time
# from test import decToBinList


# GPIO.setmode(GPIO.BCM)

# leds = [10, 9, 11, 5, 6, 13, 19, 26][::-1]



# while True:
#     print("Введите значение от 0 до 255(-1 для выхода): ")
#     try:
#         value = int(input())
#     except ValueError:
#         print("Некорректное значение. Попробуйте ещё раз.")
#         continue
#     if value == -1:
#         GPIO.cleanup()
#         exit()
#     elif 0 <= value <= 255:
#         break
# num2dac(value)
# print("Для продолжения нажмите Enter, для выхода -1: ")
# while input() != '-1':
#     main()


# def num2dac(value, slee_time = 20):
#     dac = [leds[x] for x in range(8) if decToBinList(value)[x] == 1]
#     GPIO.setup(dac, GPIO.OUT)
#     GPIO.output(dac, 1)
#     time.sleep(slee_time)
#     GPIO.output(dac, 0)


    