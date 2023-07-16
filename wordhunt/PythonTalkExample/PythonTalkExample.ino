
int x;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  if(Serial.available()){
    x = Serial.readString().toInt();
    Serial.print(x + 1);
  }
}
