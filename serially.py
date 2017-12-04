#!/usr/bin/env python
import serial, time
from pynput import keyboard
import cv2
from threading import Thread

ser = None
finished = False
started = False

try:
        ser = serial.Serial('/dev/ttyACM0',9600)
except Exception as e:
        ser = serial.Serial('/dev/ttyACM1',9600)
def on_release(key):
	global started, finished
	if key == keyboard.Key.esc:
		started = True
		finished = True
		return False
	special_flag = False
	for k in keyboard.Key:
		if k == key:
			special_flag = True
			print('Pressed a special key')
	if not special_flag:
		try:
			print('The key pressed was {0}'.format(key.char))
			ser.flushInput()
			ser.write(key.char.encode())
			started = True
		except Exception as e:
			print('Threw an exception!!!!! :C',e)

def read_images():
    print('Pop a cap in dat ass')
    cap = cv2.VideoCapture(0)
    while True:
		if started and finished:
			break
		if started and not finished:
			print('Lets get it started hah!')
			index = 0
			while(not finished):
				print('Do the running man')
				ret, frame = cap.read()
				cv2.imwrite('serially_image{0}.png'.format(index),frame)
				index +=1
    cap.release()
    return True
	
time.sleep(1)
# Collect events until released
capture_thread = Thread(target=read_images)
capture_thread.start()
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
    capture_thread.join()
