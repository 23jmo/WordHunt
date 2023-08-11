
# WordHunt Bot

Arduino-powered bot that holds the world record score for the GamePigeon Word Hunt game. 

- 4x4 Board Record: 228k 
- 5x5 Board Record: WIP




## Demo





## Materials

- Arduino Micro (Or any arduino or any model with Mouse library support)
- Arduino Uno (Or any arduino model)
- iPhone to play Word Hunt with assitive touch enabled (this allows Mouse control)
- Computer where code is run
- Associated cables (USB to Arduino Uno, Arduino Uno to Arduino Micro, Arduino Micro to Lightning, and a dongle if necessary) 

## Setup

To use the bot yourself:

```bash
1. Install the Arduino App on your computer
2. Clone this GitHub repository using 
3. Upload the SerialSender file to the Arduino Uno
4. Upload the SerialReceiver file to the Arduino Micro
5. Connect the 9 port on the Arduino Uno to the 8 port on the Arduino Micro
6. Connect the 8 port on the Arduino Uno to the 9 port on the Arduino Micro
7. Connect the Ground (Gnd) port of the two Arduino together
8. Enable assistive touch on the phone that will be playing Word Hunt
9. Connect Computer to Arduino Uno, Arduino Micro to iPhone (two arduinos already connected)
10. Run the [] file on your Computer
11. Input the board by reading left to right, top to bottom 
12. Once you hit enter, the bot will start playing the game!
```


## Features

- Finds Maximum Possible Score of the Board
- Live Progress and expected score
- Auto Recallibration 

