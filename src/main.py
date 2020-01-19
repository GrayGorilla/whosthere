import time
from gpiozero import MotionSensor
from camera import personOrPackage 

pir = MotionSensor("BOARD7")

while True:
    # Detecting Motion
    motion = pir.motion_detected
    if (motion):
        print("Motion Detected")
        fileName, person, package = personOrPackage()
        print("Person present?: ", person)
        print("Package present?: ", package)
    else:
        print("No Motion")
    time.sleep(1)

