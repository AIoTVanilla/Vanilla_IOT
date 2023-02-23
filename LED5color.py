import RPi.GPIO as IoPort
import RPi.GPIO as GPIO
import time

def led_off():
    IoPort.output(red_pin, False)
    IoPort.output(yellow_pin, False)
    IoPort.output(white_pin, False)
    IoPort.output(blue_pin, False)
    IoPort.output(green_pin, False)

def led_on(pin, delay):
    led_off()
    IoPort.output(pin, True)
    time.sleep(delay)

red_pin = 19
yellow_pin = 6
white_pin = 5
blue_pin = 21
green_pin = 20

IoPort.setmode(IoPort.BCM)
IoPort.setup(red_pin, IoPort.OUT)
IoPort.setup(yellow_pin, IoPort.OUT)
IoPort.setup(white_pin, IoPort.OUT)
IoPort.setup(blue_pin, IoPort.OUT)
IoPort.setup(green_pin, IoPort.OUT)

time.sleep(0.8)
no = 0.1

while no < 1:
    led_on(red_pin, 0.8)
    led_on(yellow_pin, 0.8)
    led_on(white_pin, 0.8)
    led_on(blue_pin, 0.8)
    led_on(green_pin, 0.8)
    no += 0.1