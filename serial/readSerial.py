import serial
import sys

ser = serial.Serial(
    port='/dev/ttyUSB2',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
while True:
   buff = ser.read(10000)
   if len(buff) > 0:
      sys.stdout.write(buff)

ser.close()
