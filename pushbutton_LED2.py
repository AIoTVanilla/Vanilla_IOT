import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

try:
    while True:
        inputIO = GPIO.input(21)
        
    if inputIO == False:
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        
    else:
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        
except KeyboardInterrupt:
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.cleanup()