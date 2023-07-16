int data = -1; 

int inputByte;

#include <SoftwareSerial.h> 
SoftwareSerial MyBlue(10, 11);

void setup() {
  Serial.begin(9600);
  MyBlue.begin(9600);
  Serial.setTimeout(1);
  Serial.println("Bluetooth Connected");
}


void loop() {
  if(MyBlue.available()){
    inputByte = MyBlue.read();
    MyBlue.print(inputByte);
  }
  else{
    Serial.println("not available");
  }
//  while(!MyBlue.available());
//  data = MyBlue.readString().toInt();
//  MyBlue.write(data + 1);
//  delay(100);
//  while (!Serial.available());
//  //int y = Serial.readString().toInt();
//  x = char(Serial.readString().toInt());
//  Serial.print(x);
//  Serial.write(x);
//  delay(20);
  //Serial.print(swipes[x]);
}
