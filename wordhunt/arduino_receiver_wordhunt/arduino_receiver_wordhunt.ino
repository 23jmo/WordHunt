char data;
String swipes[8] = {"up", "upright", "right", "downright", "down", "downleft", "left", "upleft"};

void setup() {
  Serial.begin(9600);
  Serial.println("working");
}

void loop() {
  if(Serial.available())
  {
    //Serial.println("looking");
    data = Serial.read(); //Read the serial data and store in var
    Serial.println(data); //Print data on Serial Monitor
  }
  else{
    Serial.println("receiver serial not available");
  }
  delay(100);
  
}
