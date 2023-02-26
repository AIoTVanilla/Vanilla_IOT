import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 17
ECHO = 18
LED_R = 24
LED_B = 9

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

def getDistance():
    try:
        GPIO.output(TRIG, False)
        time.sleep(1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end-pulse_start
        distance = round(pulse_duration*17150,2)
        return distance
    except:
        return None

if __name__ == '__main__':
    try:
        while True:
            distance_value = getDistance()
            if distance_value != None:
                if distance_value > 2 and distance_value < 35:
                    print("Distance is %.2f cm" %distance_value)
                    GPIO.output(LED_R, GPIO.HIGH)
                    GPIO.output(LED_B, GPIO.LOW)
                else:
                    print("Out of Range %.2f cm" %distance_value)
                    GPIO.output(LED_B, GPIO.HIGH)
                    GPIO.output(LED_R, GPIO.LOW)
                
    except KeyboardInterrupt:
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        GPIO.cleanup()