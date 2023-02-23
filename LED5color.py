import RPi.GPIO as IoPort
import RPi.GPIO as GPIO
import time
import socketio

sio = socketio.Client()
red_pin = 19
yellow_pin = 6
white_pin = 5
blue_pin = 21
green_pin = 20

@sio.on('snack_list')
def snack(items):
    print('snack', items)
    led_off()
    has_chicken = "chicken_legs" in items
    has_kancho = "kancho" in items
    has_rollpoly = "rollpoly" in items
    has_ramen_snack = "ramen_snack" in items
    has_whale_food = "whale_food" in items
    if has_chicken: led_on(red_pin, 0.8)
    if has_kancho: led_on(yellow_pin, 0.8)
    if has_rollpoly: led_on(white_pin, 0.8)
    if has_ramen_snack: led_on(blue_pin, 0.8)
    if has_whale_food: led_on(green_pin, 0.8)

def led_off():
    IoPort.output(red_pin, False)
    IoPort.output(yellow_pin, False)
    IoPort.output(white_pin, False)
    IoPort.output(blue_pin, False)
    IoPort.output(green_pin, False)

def led_on(pin, delay):
    # led_off()
    IoPort.output(pin, True)
    # time.sleep(delay)

if __name__ == "__main__":
    IoPort.setmode(IoPort.BCM)
    IoPort.setup(red_pin, IoPort.OUT)
    IoPort.setup(yellow_pin, IoPort.OUT)
    IoPort.setup(white_pin, IoPort.OUT)
    IoPort.setup(blue_pin, IoPort.OUT)
    IoPort.setup(green_pin, IoPort.OUT)

    time.sleep(0.8)
    sio.connect('ws://192.168.50.200:7777')

    while True:
        pass
        # led_on(red_pin, 0.8)
        # led_on(yellow_pin, 0.8)
        # led_on(white_pin, 0.8)
        # led_on(blue_pin, 0.8)
        # led_on(green_pin, 0.8)