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

  pinMode(LED_BUILTIN, OUTPUT);  

//  println(Serial.list()); // List COM-ports
//  
//  // CAN WE USE THIS IN PYTHON/C++ TO PREVENT PORT UPDATE PROBLEM??
//  port = new Serial(this, Serial.list()[1], 19200); //select second com-port from the list
  Serial.begin(9600);
  delay(1);
  DRIVE.write(90);
  TURN.write(90);
  
}

void loop() {
  delay(1);
  if (Serial.available()) {
    int val = Serial.read();
    Serial.println(val);
    switch (val) {
      
      // full left turn
      case 'a':
      {
//        TURN.writeMicroseconds(2200);   // FULL RIGHT TURN HITS ROBOT GUARD
        TURN.write(170);
        digitalWrite(LED_BUILTIN, HIGH);
        break;
      }
  
      // half left turn
      case 'q':
      {
//        TURN.writeMicroseconds(1850);
        TURN.write(135);
        digitalWrite(LED_BUILTIN, LOW);
        break;
      }
  
      //full right turn
      case 'd':
      {
//        TURN.writeMicroseconds(800);
        TURN.write(15);       // FULL RIGHT TURN HITS ROBOT GUARD
        break;
      }
  
      // half right turn
      case 'e':
      {
//        TURN.writeMicroseconds(1150);
        TURN.write(45);
        break;
      }
  
      // go straight
      case 'w':
      {
//        TURN.writeMicroseconds(1400);
          TURN.write(90);
        break;
      }
  
      // full reverse
      case 'm':
      {
//        DRIVE.writeMicroseconds(1000);
        DRIVE.write(0);
        break;
      }
  
      // half reverse
      case 'n':
      {
//        DRIVE.writeMicroseconds(1350);
        DRIVE.write(135);
        break;
      }
  
      // STOP
      case 'b':
      {
//        DRIVE.writeMicroseconds(1430);
        DRIVE.write(90);
        break;
      }
  
      // half forward
      case 'v':
      {
//        DRIVE.writeMicroseconds(1600);
        DRIVE.write(45);
        break;
      }
      // full forward
      case 'c':
      {
//        DRIVE.writeMicroseconds(2000);
        DRIVE.write(0);
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

