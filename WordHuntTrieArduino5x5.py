
from more_itertools import sort_together
import serial
import time

#arduino = serial.Serial(port='/dev/cu.usbmodem21101', baudrate=115200, timeout=.1)
#arduino = serial.Serial(port='/dev/cu.usbmodem11301', baudrate=115200, timeout=.1)
arduino = serial.Serial(port='/dev/cu.usbmodem21301', baudrate=9600, timeout=0)

#define the board dinensions: 
M = 5
N = 5

class Point:
    x = 0
    y = 0
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self):
     return "(" + str(self.x) + ", " + str(self.y) + ")"

POINTS = []

for i in range(M):
    ROW = []
    for j in range(N):
        ROW.append(Point(i,j))
    POINTS.append(ROW)

print(POINTS)
        

def determineSwipe(point1, point2):
    #x is row, y is col
    #0 up
    #1 upright
    #2 right
    #3 downright
    #4 down
    #5 downleft
    #6 left
    #7 upleft
    if(point2.x > point1.x): 
        if(point2.y > point1.y): 
            return 3
        if(point1.y == point2.y): 
            return 2
        else:
            return 1
    elif(point1.x == point2.x): 
        if(point2.y > point1.y):
            return 4
        else:
            return 0
    else:
        if(point2.y > point1.y): 
            return 5
        if(point1.y == point2.y):
            return 6
        else:
            return 7

def write_read(x):
    #print(x)
    arduino.write(bytes(str(x), 'utf-8'))
    #time.sleep(1)
    #time.sleep(0.4), receiver delay 50, sender delay 100
    #time.sleep(0.2), receiver delay 50, sender delay 100
    #time.sleep(0.15), receiver delay 50, sender delay 100
    #time.sleep(0.07), receiver delay 25, sender delay 50
    #time.sleep(0.06), receiver delay 25, sender delay 50
    #time.sleep(0.06), reciever delay 20, sender delay 40
    #time.sleep(0.05), reciever delay 20, sender delay 40
    #time.sleep(0.04), reciever delay 15, sender delay 30
    #time.sleep(0.03), receiver delay 12, sender delay 24 (mid)
    #time.sleep(0.032), receiver delay 12, sender delay 24 (more consistent)
    time.sleep(0.032)

def swipeRel(point1, point2):
    write_read(determineSwipe(point1, point2))

def getToNextWord(point1, point2):
    #print("getting to next word")
    x_diff = point2[1]-point1[1]
    y_diff = point2[0]-point1[0]

    first_move = min(abs(x_diff), abs(y_diff))

    x_move = 2 if x_diff > 0 else 6
    y_move = 4 if y_diff > 0 else 0

    #move by same amt in both dir
    for i in range(first_move):
        #print("moving moving")
        if(x_diff > 0):
            if(y_diff > 0):
                write_read(3)
            else:
                write_read(1)
        else:
            if(y_diff > 0):
                write_read(5)
            else:
                write_read(7)
    #finish moving

    final_move = x_move if abs(x_diff) > abs(y_diff) else y_move

    for i in range(abs(abs(x_diff) - abs(y_diff))):
        write_read(final_move)




def swipeWord(swipes):
    point1 = POINTS[swipes[0][0]][swipes[0][1]]
    write_read(8)
    for i in range(len(swipes)-1):
        point1 = POINTS[swipes[i][0]][swipes[i][1]]
        point2 = POINTS[swipes[i+1][0]][swipes[i+1][1]]
        swipeRel(point1, point2)
        #print(point1.x, point1.y, " --> ", point2.x, point2.y)
    write_read(9)



class TrieNode:
 
    # Trie node class
    def __init__(self):
        self.children = [None] * 26
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
 

ans = []
totalSwipes = []

class Boogle:
 
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
 
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self, ch):
 
        # private helper function
        # Converts key current character into index
        # use only 'A' through 'Z' and upper case
        return ord(ch) - ord('A')
 
    def insert(self, key):
 
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            # if current character is not present
            if not pCrawl.children[index]:
 
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            # print('h', self.root.children)
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
 
 
def is_Safe(i, j, vis):
    return 0 <= i < M and 0 <= j < N and not vis[i][j]
 

def search_word(root, boggle, i, j, vis, string, swipes):

    if root.isEndOfWord and string not in ans:
        ans.append(string)
        totalSwipes.append(swipes)
 
    if is_Safe(i, j, vis):
        vis[i][j] = True
        for K in range(26):
            if root.children[K] is not None:
                ch = chr(K+ord('A'))
                # print(i, j, " : ", ch)
                # Recursively search reaming character of word
                # in trie for all 8 adjacent cells of boggle[i][j]
                if is_Safe(i + 1, j + 1, vis) and boggle[i + 1][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j + 1, vis, string + ch, swipes +[(i+1,j+1)])
                if is_Safe(i, j + 1, vis) and boggle[i][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i, j + 1, vis, string + ch, swipes + [(i,j+1)])
                if is_Safe(i - 1, j + 1, vis) and boggle[i - 1][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j + 1, vis, string + ch, swipes + [(i-1,j+1)])
                if is_Safe(i + 1, j, vis) and boggle[i + 1][j] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j, vis, string + ch, swipes + [(i+1,j)])
                if is_Safe(i + 1, j - 1, vis) and boggle[i + 1][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j - 1, vis, string + ch, swipes + [(i+1,j-1)])
                if is_Safe(i, j - 1, vis) and boggle[i][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i, j - 1, vis, string + ch, swipes + [(i,j-1)])
                if is_Safe(i - 1, j - 1, vis) and boggle[i - 1][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j - 1, vis, string + ch, swipes + [(i-1,j-1)])
                if is_Safe(i - 1, j, vis) and boggle[i - 1][j] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j, vis, string + ch, swipes + [(i-1,j)])
        vis[i][j] = False
 
 
def char_int(ch):
   
    # private helper function
    # Converts key current character into index
    # use only 'A' through 'Z' and upper case
    return ord(ch) - ord('A')
 
 
def findWords(boggle, root):
   
    # Mark all characters as not visited
    visited = [[False for i in range(N)] for i in range(M)]
 
    pChild = root
 
    string = ""
 
    # traverse all matrix elements
    for i in range(M):
        for j in range(N):
            # we start searching for word in dictionary
            # if we found a character which is child
            # of Trie root
            if pChild.children[char_int(boggle[i][j])]:
                # print('h')
                string = string + boggle[i][j]
                swipes = [(i,j)]
                # print(i, j, " : ", string)
                search_word(pChild.children[char_int(boggle[i][j])],
                            boggle, i, j, visited, string, swipes)
                string = ""
    
dictionary = []

with open("WordHuntWords.txt") as words:
    dictionary = words.read().splitlines()

# root Node of trie
t = Boogle()
 
# insert all words of dictionary into trie
n = len(dictionary)
for i in range(n):
    t.insert(dictionary[i])

root = t.root
seq = input("What is the board? (arduino)")
while(len(seq) != 25):
    seq = input("What is the board?")


#TODO: Start A Timer Python

start_time = time.time()


board = []
index = 0
for i in range(5):
    row = []
    for j in range(5):
        row.append(seq[index])
        index+=1
    board.append(row)

    
# board = [['T', 'K', 'A', 'T'],
#           ['O', 'C', 'E', 'F'],
#           ['A', 'G', 'S', 'W'],
#           ['R', 'O', 'U', 'R']]
 
# print(root.children)

findWords(board, root)



ans2, totalSwipes2 = sort_together([ans, totalSwipes], key=len, reverse= True)

maxPossibleScore = 0
exp_score = 0
def calcScore(length):
    if length == 3:
        return 100
    elif length == 4:
        return 400
    elif length == 5:
        return 800
    elif length >= 6:
        return 1400 + (length - 6) * 400

for word in ans2:
    maxPossibleScore += calcScore(len(word))

print("===================")
print("total words: ", len(ans2))
print("max possible score: ", maxPossibleScore)
print("-------------------")

getToNextWord((0,0), (totalSwipes2[0][0]))

reset_value = len(ans2[0])
#get the words
for i in range(len(ans2)):
    swipes = totalSwipes2[i]
    exp_score += calcScore(len(swipes))
    print(str(i+1) + "/" + str(len(ans2)) + ", exp score: " + str(exp_score) + "/" + str(maxPossibleScore) + " Getting " + str(ans2[i]) + " : " + str(totalSwipes2[i]))
    #somehow get to next word -> maybe get rid of encapsulated method swipeWord
    #print(POINTS[swipes[0][0]][swipes[0][1]])
   
    #swipeWord(swipes)
   
    ### following does what swipeWord does
    point1 = POINTS[swipes[0][0]][swipes[0][1]]
    write_read(8)
    for j in range(len(swipes)-1):
        point1 = POINTS[swipes[j][0]][swipes[j][1]]
        point2 = POINTS[swipes[j+1][0]][swipes[j+1][1]]
        swipeRel(point1, point2)
    write_read(9)
    ###
    
    reset_num = (reset_value - len(ans2[i]) + 2)
    if(i > 0 and i % reset_num == 0):
        #fix offset
        print("fixing offset every" + str(reset_num))
        write_read('a') #zero at top left char
        time.sleep(0.1)
        if(i+1 < len(ans2)):
            getToNextWord((0,0), totalSwipes2[i+1][0])
        
    else:
        if(i+1 < len(ans2)):
            getToNextWord(swipes[len(swipes)-1], totalSwipes2[i+1][0])

write_read('a')


 
