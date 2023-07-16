from platform import python_branch
import pyautogui
import time
import WordHuntTrieArduino4x4

class Point:
    x = 0
    y = 0
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
time.sleep(3)
print(pyautogui.size())

POINTS = [
          [Point(504, 320), Point(604, 320), Point(704, 320), Point(804, 320)],
          [Point(504, 420), Point(604, 420), Point(704, 420), Point(804, 420)],
          [Point(504, 520), Point(604, 520), Point(704, 520), Point(804, 520)],
          [Point(504, 620), Point(604, 620), Point(704, 620), Point(804, 620)]
         ]

def swipeRel(point1, point2):
    pyautogui.dragRel(point2.x - point1.x, point2.y - point2.y, 0.1)

def swipeWord(swipes):
    pyautogui.moveTo(POINTS[swipes[0][1][0],swipes[0][1][1]])
    #pyautogui.click()
    for i in range(len(swipes)-1):
        swipeRel(POINTS[swipes[i][1][0], swipes[i][1][1]], POINTS[swipes[i+1][1][0], swipes[i+1][1][1]])
    
