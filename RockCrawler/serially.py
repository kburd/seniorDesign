#!/usr/bin/env python
import serial, time
from pynput import keyboard
import cv2
from threading import Thread
import os, errno

DIR_NAME='drive_images'

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

# def read_images():
#     new_dir = os.getcwd()+'/'+DIR_NAME
#     try:
#         if not os.path.isdir(new_dir):
#             os.makedirs(new_dir)
#     except OSError as e:
#         print(e)
#     print('Pop bottles')
#     cap = cv2.VideoCapture(0)
#     while True:
# 		if started and finished:
# 			break
# 		if started and not finished:
# 			print('Lets get it started, hah!')
# 			index = 0
# 			while(not finished):
# 				ret, frame = cap.read()
# 				if not frame is None:
#                                     cv2.imwrite('{1}/serially_image{0}.png'.format(index,DIR_NAME),frame)
# 				index +=1
#     cap.release()
#     return True
	
time.sleep(1)
# Collect events until released
# capture_thread = Thread(target=read_images)
# capture_thread.start()
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
    capture_thread.join()
