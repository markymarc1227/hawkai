import time
import serial

serialcomm = serial.Serial("COM3",9600)
time.sleep(2)

#Accident
def accident(info):
    print("Accident Detected!")
    serialcomm.write(info.encode('utf-8'))

def reset():
    print("Resetting..")
    serialcomm.write(b"0\r\n")

x = int(input("Activate Alarm? "))
if x == 1:
    accident("212:00AMStreet 12 Baranggay 12 Near Pasay City")

y = int(input("Disable Alarm?: "))
if y == 2:
    reset()

