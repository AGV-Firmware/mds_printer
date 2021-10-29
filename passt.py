import serial

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
ser.parity=serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1
i = 0
Test = 'Dummy'
ser.open()
while i< 50:
  if ser.in_waiting:
    Test = ser.readline()
    Data =  b'TEXT 10,30,\"3\",0,1,1,\"' + Test +'\"\n' 
    printer_test(ser,Data)
#Data =  b'TEXT 10,30,\"3\",0,1,1,\"' + Test +'\"\n' 


def printer_test(ser,Data):
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write('DIRECTION 1\n');
  ser.write(b'CLS\n');
  ser.write(Data)
  ser.write(b'PRINT 1\n')



