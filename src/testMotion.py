from gpiozero import MotionSensor

pir = MotionSensor("BOARD7")

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    pir.wait_for_no_motion()
    print("No Motion")
