

from pynmea import nmea
import serial, time, sys, threading, datetime, shutil
######Global Variables#####################################################
# you must declare the variables as 'global' in the fxn before using#
ser = 0
lat = 0
long = 0
pos_x = 0
pos_y = 0

#BAUDRATE is GPS dongle specific but usually 4800
BAUDRATE = 4800

######FUNCTIONS############################################################ 

def check_serial():
	print ('Sam is assuming you plugged in the USB receiver. I will ask you what port you plugged it into now :D')
	init_serial()
	
def init_serial():
	#opens the serial port based on the COM number you choose
	print ("Found Ports:")
	#the next three lines are supposed to scan for the possible ports the GPS is plugged into
	#for n,s in scan():
#		print "%s" % s
	#print " "
        
        
	#enter your COM port number
	print ("Choose a COM port #. Enter # only, then enter")
	temp = input() #waits here for keyboard input
	if temp == 'e':
		sys.exit()
	comnum = '/dev/ttyUSB' + temp #concatenate COM and the port number to define serial port

	# configure the serial connections 
	global ser, BAUDRATE
	ser = serial.Serial()
	ser.baudrate = BAUDRATE
	ser.port = comnum
	ser.timeout = 1
	ser.open()
	ser.isOpen()
	
	#Prints menu and asks for input

	print ('OPEN: '+ ser.name)
	print ('')
	
def scan():
    #scan for available ports. return a list of tuples (num, name)
    available = []
    for i in range(256):
        try:
            s = serial.Serial(str(i))
            available.append( (i, s.name))
            s.close()   # explicit close 'cause of delayed GC in java
        except serial.SerialException:
            pass
    
    return available  

def getLatLong()
		try:
			data = ser.readline()
			data = data.decode("utf-8")#converts data from bytes to string for parsing
			if (data[0:6] == '$GPGGA'):
				gpgga = nmea.GPGGA()
				gpgga.parse(data)
				lats = gpgga.latitude
				longs = gpgga.longitude
			
				#convert degrees, decimal minutes to decimal degrees 
				lat1 = (float(lats[2]+lats[3]+lats[4]+lats[5]+lats[6]+lats[7]+lats[8]))/60
				lat = (float(lats[0]+lats[1])+lat1)
				long1 = (float(longs[3]+longs[4]+longs[5]+longs[6]+longs[7]+longs[8]+longs[9]))/60
				long = (float(longs[0]+longs[1]+longs[2])+long1)			

				#calc position
				pos_y = lat
				pos_x = -long		
	
#				print(pos_y)
#				print(pos_x)
#				print(pos_y + ',' + pos_x)
#				latLong[0] = (pos_y)
#				latLong[1] = (pos_x)
				latLongString = (str(pos_y) + ',' + str(pos_x))
#				print(latLongString)
				return latLongString
			else:
#				print('Not GPGGA line')
				return getLatLong()
		except:
#			pass
			return getLatLong()
#			print('I FAILED YOU ANAKIN')

########START#####################################################################################
check_serial()
#getLatLong()
test = getLatLong()
#print(test)
#ser.close()
#sys.exit()
