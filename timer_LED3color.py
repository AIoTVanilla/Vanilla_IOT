import RPi.GPIO as IoPort
import RPi.GPIO as GPIO
import time

def State_1(Delay):
    IoPort.output(Port1, True)
    IoPort.output(Port3, False)
    time.sleep(Delay)
    
def State_2(Delay):
    IoPort.output(Port2, True)
    IoPort.output(Port1, False)
    time.sleep(Delay)
    
def State_3(Delay):
    IoPort.output(Port3, True)
    IoPort.output(Port2, False)
    time.sleep(Delay)
    
Port1 = 5
Port2 = 6
Port3 = 19

IoPort.setmode(IoPort.BCM)
IoPort.setup(Port1, IoPort.OUT)
IoPort.setup(Port2, IoPort.OUT)
IoPort.setup(Port3, IoPort.OUT)
time.sleep(0.8)
no = 0.1

while no < 1:
    State_1(0.8)
    State_2(0.8)
    State_3(0.8)
    no += 0.1