
#include <SoftwareSerial.h>
SoftwareSerial link(10,11);

char text[20];

void setup() {
  // put your setup code here, to run once:
  link.begin(9600);
  Serial.begin(9600);
}

void loop() {
  strcat(text, "hello");
  Serial.println(text);
  link.println(text);
  delay(200);
}
