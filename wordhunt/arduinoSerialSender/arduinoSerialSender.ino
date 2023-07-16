
int x;

#include <SoftwareSerial.h> 
SoftwareSerial receiver(10, 11);
void setup() {
  Serial.begin(115200);
  receiver.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  if(Serial.available()){
    x = Serial.readString().toInt();
    Serial.print(x + 1);
    receiver.write(x);
    receiver.println("sent");
  }
  else{
    receiver.println("no");
  }
  delay(100);
}
