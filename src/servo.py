#Servo.py

import RPi.GPIO as GPIO
import time

P_SERVO = 2 # adapt to your wiring
fPWM = 50 # Hz (not higher with software PWM)
a = 10
b = 2

def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(P_SERVO, GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)
    time.sleep(1) # allow to settle

def open():
    print("Open starting")
    setDirection(0)
    print("Open done")

def close():
    print("Close starting")    
    for direction in range(180, 0, -180):
        setDirection(direction)
    print("Close done")

def run():
    setup()
    open()
    close()
    


