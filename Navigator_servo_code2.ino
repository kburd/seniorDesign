#include <Servo.h>

Servo TURN;
Servo DRIVE;
//Assigns pin to servo
int motorOnePin = 3;
int motorTwoPin = 5;
int LEDpin = 13;

void setup() {
  //Sets up connection to servo
  TURN.attach(motorOnePin);
  DRIVE.attach(motorTwoPin);

//  TURN.writeMicroseconds(1500);
//  DRIVE.writeMicroseconds(1430);    // 1430

  pinMode(LED_BUILTIN, OUTPUT);  

//  println(Serial.list()); // List COM-ports
//  
//  // CAN WE USE THIS IN PYTHON/C++ TO PREVENT PORT UPDATE PROBLEM??
//  port = new Serial(this, Serial.list()[1], 19200); //select second com-port from the list

  Serial.begin(9600);
  
  
  
}

void loop() {
  
  if (Serial.available()) {
    int val = Serial.read();
//    val = 'v';
    Serial.println(val);
    switch (val) {
      
      // full left turn
      case 'a':
      {
        TURN.writeMicroseconds(2200);   // use "TURN.write(x)" instead, 0 < x < 180 degrees
        digitalWrite(LED_BUILTIN, HIGH);
        break;
      }
  
      // half left turn
      case 'q':
      {
        TURN.writeMicroseconds(1850);
        digitalWrite(LED_BUILTIN, LOW);
        break;
      }
  
      //full right turn
      case 'd':
      {
        TURN.writeMicroseconds(800);
        break;
      }
  
      // half right turn
      case 'e':
      {
        TURN.writeMicroseconds(1150);
        break;
      }
  
      // turn straight
      case 'w':
      {
        TURN.writeMicroseconds(1400);
        break;
      }
  
      // full forward
      case 'm':
      {
        DRIVE.writeMicroseconds(1000);
        break;
      }
  
      // half forward
      case 'n':
      {
        DRIVE.writeMicroseconds(1350);
        break;
      }
  
      // STOP
      case 'b':
      {
        DRIVE.writeMicroseconds(1430);
        break;
      }
  
      // half reverse
      case 'v':
      {
        DRIVE.writeMicroseconds(1600);
        break;
      }
      // full reverse
      case 'c':
      {
        DRIVE.writeMicroseconds(2000);
        break;
      }
    }
  }
}

//void turn( float angle){
//
//  float ratio = angle/45;
//  myServo.writeMicroseconds(1500 - ratio*500);
//
//}

