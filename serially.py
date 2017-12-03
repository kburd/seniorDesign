import serial, time

ser = serial.Serial('/dev/ttyACM1',9600)
time.sleep(1)
while True:
	new_ser = raw_input('input a character: ')
	print type(new_ser), new_ser
	if new_ser == 'p':
		break
	try:
		ser.flushInput()
		ser.write(new_ser)
	except Exception as e:
		print('Exception',e)
#ser.close()
