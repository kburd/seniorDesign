#Simple socket server using threads
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse,parse_qs
import serial
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(20, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH)

def updateWheels(speed,direction):
    
    if( direction == "straight" and speed == "stop"):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        return
    
    if(speed == "go"):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        
    elif(speed == "stop"):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        
    if(direction == "left"):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        
    elif(direction == "right"):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)
        
    elif(direction == "straight"):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        
    
        


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):

        par = parse_qs(urlparse(self.requestline).query)
        
        print(par)
        
        speed = par['speed'][0];
        direction = par['direction'][0];
        
        
        try:
        
            updateWheels(speed,direction)
        
        except Exception as e:
            
            message = e;
            print(e)
            
        # Send response status code
        self.send_response(204)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        # Send message back to client
        #message = "Recieved"
        # Write content as utf-8 data
        #self.wfile.write(bytes(message, "utf8"))
        return

def run():
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('0.0.0.0', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

  
        
  print('running server...')
  httpd.serve_forever()


run()
