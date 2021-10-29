import serial

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
ser.parity=serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1

ser.open()
ser.write()


