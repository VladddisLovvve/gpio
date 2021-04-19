from time import sleep
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt


GPIO.setmode(GPIO.BCM)

ledTransfer = {0:10, 1:9, 2:11, 3:5, 4:6, 5:13, 6:19, 7:26}


def num2dac(value, sl_time = 10):
    binNumber = bin(value)[2:]
    binNumber = [int(x) for x in binNumber]
    i = 8 - len(binNumber)
    binNumber = [0]*i + binNumber
    d = list(ledTransfer.values())[::-1]
    d = [d[x] for x in range(len(d)) if binNumber[x] != 0]
    GPIO.setup(d, GPIO.OUT)
    GPIO.output(d, 1)
    time.sleep(sl_time)
    GPIO.output(d, 0)
    
def sin(time, frequency):
    time = np.arange(0, time, 1 / frequency)
    y = 255 * np.sin(time)
    amplitude = [int(x) for x in y]
    plt.plot(time, amplitude)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()
    for value in amplitude:
        num2dac(value, 1/frequency)
        
try:
    time, frequency = map(int, input().split())
    sin(time, frequency)
    
finally:
    GPIO.cleanup()
