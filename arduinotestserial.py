from readline import write_history_file
import serial
import time

port = '/dev/tty.DSDTECHHC-05'
BAUD = 9600
arduino = serial.Serial(port='/dev/cu.usbmodem1201', baudrate=9600, timeout=0)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
    
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value




