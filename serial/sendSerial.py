import serial
import sys
import time


ser = serial.Serial(
    port='/dev/ttyS0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)

print("connected to: " + ser.portstr)
i = 0x00
while True:
    #ser.write("robot")
    ser.write(chr(i))
    i = i+1
    if(i>0xff):
	i = 0x00
    time.sleep(1.0)
ser.close()
