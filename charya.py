
#!/usr/bin/python3
import os 
import time
from gpiozero import MotionSensor
pir = MotionSensor(4)# this number 4 indicates the pin connected in the raspberry pi
while True:
    if pir.motion_detected:
        print("perimeter breached code red")# this text is printed when motion is decteted from PIR sensor and it captures the image
        b=1
        cmd="fswebcam -F 3 --fps 20 -r 800x600 cam"+str(b)+ ".jpg"
        os.system(cmd)