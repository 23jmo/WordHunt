#include <Manchester.h>
#define RX_PIN 0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  man.setupReceive(RX_PIN, MAN_1200);
  man.beginReceive();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(man.receiveComplete()){
    uint16_t swipe = man.getMessage();
    man.beginReceive();
    Serial.println(swipe);
  }
  else{
    Serial.println("never received");
  }
}
