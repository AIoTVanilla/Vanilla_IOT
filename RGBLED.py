import RPi.GPIO as GPIO
import time

pins = (18, 19, 21)

def led(pins, color, t):
	RGBs = (
		(1, 1, 1),
		(1, 0, 0),
		(0, 1, 0),
		(0, 0, 1),
		(0, 1, 1),
		(1, 0, 1),
		(1, 1, 0),
	)
	
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(pins[0], GPIO.OUT)
	GPIO.setup(pins[1], GPIO.OUT)
	GPIO.setup(pins[2], GPIO.OUT)

	GPIO.output(pins[0], RGBs[color][0])
	GPIO.output(pins[1], RGBs[color][1])
	GPIO.output(pins[2], RGBs[color][2])

	time.sleep(t)

	GPIO.cleanup(pins)

led(pins, 4, 10)