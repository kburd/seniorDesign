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

  pinMode(LED_BUILTIN, OUTPUT);

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

  //Straight
  if( !bitOne & !bitTwo & !bitThree ){
     TURN.write(90);
  }

  //Left
  else if( !bitOne & !bitTwo & bitThree ){
     TURN.write(155);
  }

  //Right
  // NOTE: turning too far right will cause the tierod 
  // to rub against the bumper and burn out the motor
  else if( !bitOne & bitTwo & !bitThree ){
     TURN.write(25);
  }

  //Stop & straight
  else if( !bitOne & bitTwo & bitThree ){
     DRIVE.write(90);
     TURN.write(90);
  }

  //Go
  else if( bitOne & !bitTwo & !bitThree ){
     DRIVE.write(100);
  }

  //TEST INPUT PINS - turn left, right, then straight
  else if( bitOne & bitTwo & bitThree ){
    DRIVE.write(90);

    //brief left, right, then straight
    TURN.write(155);
    delay(500);
    TURN.write(25);
    delay(500);
    TURN.write(90);

    // this is just to give visual output after pin testing
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);
    delay(200);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);
  }
  
}
