#include <Mouse.h>

#include <Keyboard_de_DE.h>
#include <Keyboard_sv_SE.h>
#include <KeyboardLayout.h>
#include <Keyboard.h>
#include <Keyboard_it_IT.h>
#include <Keyboard_fr_FR.h>
#include <Keyboard_da_DK.h>
#include <Keyboard_es_ES.h>

void leftSwipe(){
  
}
void upLeftSwipe(){
  
}
void upSwipe(){
  
}
void upRightSwipe(){
  
}
void rightSwipe(){
  
}
void downRightSwipe(){
  
}
void downSwipe(){
  
}
void downLeftSwipe(){
  
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600)
  Mouse.begin();
  Mouse.release(MOUSE_LEFT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    String msg = Serial.readString();
    if(msg == "LEFT")
  }
}
