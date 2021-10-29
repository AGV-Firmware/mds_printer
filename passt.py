import serial
def printer_test(ser,Data):
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write(b'DIRECTION 1\n');
  ser.write(b'CLS\n')
  ser.write(b'TEXT 100,30,\"4\",0,1,1,\"Microwave Disinfected Waste\"\n')
  ser.write(b'TEXT 250,75,\"2\",0,1,1,\"Lineowave Technologies"\n')
  #ser.write(b'TEXT 120,100,\"2\",0,1,1,\"Line12342353512141hfckahkjf\"\n')
  temp = "TEXT 65,200,\"3\",0,1,1,\"Date : " +Data[0]     + "  Weight :  " + Data[6]    +"    KG\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,275,\"3\",0,1,1,\"Starting Time  : " +Data[4]     + "  Device :  " + Data[2]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  #ser.write(b'TEXT 65,275,\"3\",0,1,1,\"Starting Time :             Device :       \"\n')
  temp = "TEXT 65,350,\"3\",0,1,1,\"Cycle Number:  " +Data[3]  + "\"\n"
  ser.write(temp.encode("utf-8"))
  ser.write(b'PRINT 1\n')
  
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write(b'DIRECTION 1\n');
  ser.write(b'CLS\n')
  ser.write(b'TEXT 100,30,\"4\",0,1,1,\"Cycle Information\"\n')
  ser.write(b'TEXT 250,75,\"2\",0,1,1,\"Lineowave Technologies"\n')
  temp = "TEXT 65,120,\"3\",0,1,1,\"Date : " +Data[0]     + "  Weight :  " + Data[6]    +"    KG\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,170,\"3\",0,1,1,\"Starting Time  : " +Data[4]     + "  Device :  " + Data[2]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,220,\"3\",0,1,1,\"Date : " +Data[0]     + "  Weight :  " + Data[6]    +"    KG\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,270,\"3\",0,1,1,\"Starting Time  : " +Data[4]     + "  Device :  " + Data[2]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,320,\"3\",0,1,1,\"Date : " +Data[0]     + "  Weight :  " + Data[6]    +"    KG\"\n"
  ser.write(temp.encode("utf-8"))
  
  ser.write(b'PRINT 1\n')
  
  j = 0
  while j < 9:
    #ser
    print(Data[j].encode("utf-8"))
    j += 1
            
    #ser.write(j.encode("utf-8"))
  #ser.write(Data.encode("utf-8"))
  #ser.write(b'PRINT 1\n')

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
    ser1.flushInput()
    ser1.flushOutput()
    string = (Test.decode("utf-8")).rstrip().lstrip()
    #string1 = string
    Data = string.split("#")
    print(Data)
    
    #Data =  "TEXT 10,30,\"3\",0,1,1,\"" + string1 + "\"\n" 
    printer_test(ser,Data)
    i+=1
#Data =  b'TEXT 10,30,\"3\",0,1,1,\"' + Test +'\"\n' 





