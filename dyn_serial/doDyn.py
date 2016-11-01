import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=1000000,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.open()
ser.isOpen()

print 'Press Enter to start.\r\nInsert "exit" to leave the application.'

input=1
the_swp = 0;
goal_val_h = 0x03;
goal_val_l = 0xff;
while 1 :
    # get keyboard input
    input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
	if the_swp == 0 :
		goal_val_h = 0x03
		goal_val_l = 0xff
		the_swp = 1
	else:
		goal_val_h = 0x00
		goal_val_l = 0x00
		the_swp = 0

	a_head 		= [0xff, 0xff]
	a_id 		= [0x01]
	a_len 		= [0x05]
	a_cmd 		= [0x03] # Write Data
	a_address  	= [0x1e] # Goal Pos
	a_goal_l	= [goal_val_l] # Goal low byte
	a_goal_h	= [goal_val_h] # Goal high byte
	a_sum		= [~(a_id[0] + a_len[0] + a_cmd[0] + a_address[0] + a_goal_l[0] + a_goal_h[0]) & 0xff]  # get checksum
	the_out_list 	= a_head + a_id + a_len + a_cmd + a_address + a_goal_l + a_goal_h + a_sum
	the_out 	= bytearray(the_out_list)
	print the_out_list
        print ser.write(the_out)
