int data;
#include <Manchester.h>
#define TX_PIN 1

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTimeout(1);
  man.setupTransmit(TX_PIN, MAN_1200);
}

void loop() {
  // put your main code here, to run repeatedly:
//  if(Serial.available()){
//    data = Serial.readString().toInt();
//    Serial.print(data+1);
//    man.transmit(data);
//    delay(200);
//  }
  man.transmit(5);
  Serial.println("trasmitting");
//  else{
//    Serial.println("sender not connected");
//  }
 
}
