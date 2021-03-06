import serial
def printer_test(ser,Data):
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write(b'DIRECTION 1\n');
  ser.write(b'CLS\n')
  ser.write(b'TEXT 80,50,\"4\",0,1,1,\"Microwave Disinfected Waste\"\n')
  ser.write(b'TEXT 200,95,\"3\",0,1,1,\"Lineowave Technologies"\n')
  temp = "TEXT 55,170,\"3\",0,1,1,\"Date: " +Data[0]     + "    WT B/f Cycle:  " + Data[5]    +"  KG\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 55,220,\"3\",0,1,1,\"Start Time: " +Data[2]     + "   WT A/f Cycle:  " + Data[6]    +"  KG\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 55,270,\"3\",0,1,1,\"Process No: " + Data[1]  + "   End Time : " + Data[4] + "\"\n"
  ser.write(temp.encode("utf-8"))
  ser.write(b'PRINT 1\n')
  
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write(b'DIRECTION 1\n');
  ser.write(b'CLS\n')
  ser.write(b'TEXT 100,50,\"4\",0,1,1,\"    Cycle Information\"\n')
  ser.write(b'TEXT 200,95,\"3\",0,1,1,\"Lineowave Technologies"\n')
  temp = "TEXT 65,150,\"2\",0,1,1,\"Date : " +Data[0]     + "     Weight :  " + Data[5]    +"   KG\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,180,\"2\",0,1,1,\"Start Time  : " + Data[2] +    "   Hold Start Time :  " + Data[3]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,210,\"2\",0,1,1,\"End Time    : " +Data[4]     + "   Total Time :  " + Data[10]    +"   min\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,240,\"2\",0,1,1,\"Start Temp  : " +Data[7]     + "      Temp Max :  " + Data[8]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,270,\"2\",0,1,1,\"Process No : " + Data[1]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  ser.write(b'TEXT 100,310,\"4\",0,1,1,\"      Disinfected !\"\n')
  
  ser.write(b'PRINT 1\n')
  #ser.write(b'CLS\n')
  #ser.write(b'PRINT 1\n')
  

ser = serial.Serial('/dev/ttyUSB_D1')
ser.baudrate = 9600
ser.parity=serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1

ser1 = serial.Serial('/dev/ttyUSB_D2')
ser1.baudrate = 9600
ser1.parity=serial.PARITY_NONE
ser1.bytesize = serial.EIGHTBITS
ser1.stopbits = serial.STOPBITS_ONE
ser1.timeout = 1

i = 0
Test = 'Dummy'

while True:
  if ser1.in_waiting:
    Test = ser1.readline()
    #print(Test)
    #print(type(Test))
    ser1.flushInput()
    ser1.flushOutput()
    string = (Test.decode("utf-8")).rstrip().lstrip()
    Data = string.split("#")
    #print(Data)
    printer_test(ser,Data)
    






