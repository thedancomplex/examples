#!/usr/bin/python3
import serial
ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)
	#x = ser.read()
	#s = ser.read(10)

ser.close()
ser.open()

while(True):
	line = ser.readline()
	print(line)
