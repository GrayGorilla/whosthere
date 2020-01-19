import time
from gpiozero import MotionSensor
from camera import personOrPackage 
from notification import sendEmail

pir = MotionSensor("BOARD7")

while True:
    # Detecting Motion
    motion = pir.motion_detected
    if (motion):
        print("Motion Detected")
        fileName, person, package = personOrPackage()
        print("Person present?: ", person)
        print("Package present?: ", package)
        if (person or package):
            sendEmail(fileName)
            time.sleep(10)
        
    else:
        print("No Motion")
        time.sleep(5)

