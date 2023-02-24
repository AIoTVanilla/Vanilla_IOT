from __future__ import print_function
import time
import RPi.GPIO as GPIO

def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()
        
    elapsed = stop-start
    distance = (elapsed * 34300) / 2
    
    return distance

def measure_average():
    distance1 = measure()
    time.sleep(0.1)
    distance2 = measure()
    time.sleep(0.1)
    distance3 = measure()
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 17
GPIO_ECHO = 18
GPIO_LED = 5
GPIO_LED2 = 6
GPIO_LED3 = 19

print("Ultrasonic Measurement")

GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_LED2, GPIO.OUT)
GPIO.setup(GPIO_LED3, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)

try:
    
    while True:
        
        distance = measure_average()
        print("Distance : %.1f" % distance)
        time.sleep(1)
        
        if distance <=10:
            print("LED_ON!!")
            GPIO.output(GPIO_LED, GPIO.HIGH)
            GPIO.output(GPIO_LED2, GPIO.HIGH)
            GPIO.output(GPIO_LED3, GPIO.HIGH)
        
        else:
            print("LED_OFF")
            GPIO.output(GPIO_LED, GPIO.LOW)
            GPIO.output(GPIO_LED2, GPIO.LOW)
            GPIO.output(GPIO_LED3, GPIO.LOW)
            
except KeyboardInterrupt:
    GPIO.cleanup()