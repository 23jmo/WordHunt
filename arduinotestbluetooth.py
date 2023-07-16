from readline import write_history_file
import serial
import time

port = '/dev/tty.DSDTECHHC-05'
BAUD = 9600
#arduino = serial.Serial(port='/dev/cu.usbmodem11301', baudrate=115200, timeout=.1)
bluetooth= serial.Serial(port, BAUD, timeout=.1, parity= serial.PARITY_EVEN, stopbits= 1)

# print("Connected")
# bluetooth.flushInput()
# for i in range(5):
#     print("Ping")
#     bluetooth.write(bytes(str(i), 'utf-8'))
#     input_data = bluetooth.readline()
#     print(input_data.decode())
#     time.sleep(0.1)
# bluetooth.close()
# print("Done")

def write_read(x):
    bluetooth.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = bluetooth.readline()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value





