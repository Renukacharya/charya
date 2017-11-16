#!/usr/bin/python3
import os 
import time
a=0
b=1
while a<10:
	cmd="fswebcam -F 3 --fps 20 -r 800x600 cam"	 +str(b) + ".jpg"
	os.system(cmd)
	time.sleep(5)
	a=a+1
	b=b+1