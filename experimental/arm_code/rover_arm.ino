//Arduino code to use arm control. Needs to be updated to include inverse kinematics
#include "ArmControl.h"
#include <EEPROM.h>

Armcontrol servo1; //Gripper
Armcontrol servo2; //Forearm (up and down)
Armcontrol servo3; //backarm (back and forth)
Armcontrol servo4; //base(left and right)

int potpin1 = 0;// Gripper is A0
int potpin2 = 0;// Forearm is A1
int potpin3 = 0;// backarm is A2
int potpin4 = 0;// base is A3

int val1;
int val2;
int val3;
int val4;

byte mode;

void setup()
{
  //Attaches servos to the i/o pins
  servo1.attach(11);
  servo1.attach(10);
  servo1.attach(9);
  servo1.attach(6); //software is now connected to hardware
  
  Serial.begin(9600); //Serial moniter will start in .96 seconds
  Serial.write("begin"); //Output to let you know it has started
}

void loop()
{
  static int v = 0; //use static so the value stays the same after loops
  
  if (Serial.available()) //If anything is typed in the serial moniter
  {
    char ch = Serial.read();
    switch(ch) {
      case '0'...'9': //from 0-9
      v = v * 10 + ch - '0';
      Serial.print(v);
      
      break;
    case 'a':
    {
    }
  }
  
  
}
//To be continued
