#include <Servo.h>

Servo TURN;
Servo DRIVE;

//Assigns pin to servo
int motorOnePin = 3;
int motorTwoPin = 5;

int commPinOne = 9;
int commPinTwo = 10;
int commPinThree = 11; 

void setup() {
  // put your setup code here, to run once:

  //Sets up connection to servo
  TURN.attach(motorOnePin);
  DRIVE.attach(motorTwoPin);

  //Assigns input/output to pins
  pinMode(commPinOne, INPUT);
  pinMode(commPinTwo, INPUT);
  pinMode(commPinThree, INPUT);

  delay(1);
  DRIVE.write(90);
  TURN.write(90);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  delay(1);
  bool bitOne = digitalRead(commPinOne);
  bool bitTwo = digitalRead(commPinTwo);
  bool bitThree = digitalRead(commPinThree);

  //Left
  if( !bitOne & !bitTwo & !bitThree ){
     TURN.write(155);
  }

  //Stright
  else if( !bitOne & !bitTwo & bitThree ){
     TURN.write(90);
  }

  //Right
  else if( !bitOne & bitTwo & !bitThree ){
     TURN.write(25);
  }

  //Stop
  else if( !bitOne & bitTwo & bitThree ){
     DRIVE.write(90);
  }

  //Go
  else if( bitOne & !bitTwo & !bitThree ){
     DRIVE.write(5);
  }

  //Reset
  else if( bitOne & bitTwo & bitThree ){
    DRIVE.write(90);
    TURN.write(90);
  }
  
}
