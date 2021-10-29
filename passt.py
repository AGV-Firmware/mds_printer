import serial
def printer_test(ser,Data):
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write(b'DIRECTION 1\n');
  ser.write(b'CLS\n');
  ser.write(bytes(Data, 'utf-8'))
  ser.write(b'PRINT 1\n')

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
ser.parity=serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1

ser1 = serial.Serial('/dev/ttyUSB1')
ser1.baudrate = 9600
ser1.parity=serial.PARITY_NONE
ser1.bytesize = serial.EIGHTBITS
ser1.stopbits = serial.STOPBITS_ONE
ser1.timeout = 1

i = 0
Test = 'Dummy'
#ser.open()
#ser1.open()

while i< 20:
  if ser1.in_waiting:
    Test = ser1.readline()
    print(Test)
    print(type(Test))
    #Data =  "TEXT 10,30,\"3\",0,1,1,\"" + String(Test) + "\"\n" 
    #printer_test(ser,Data)
    i+=1
#Data =  b'TEXT 10,30,\"3\",0,1,1,\"' + Test +'\"\n' 





