import serial
def printer_test(ser,Data):
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write(b'DIRECTION 1\n');
  ser.write(b'CLS\n')
  ser.write(b'TEXT 80,50,\"4\",0,1,1,\"Microwave Disinfected Waste\"\n')
  ser.write(b'TEXT 200,95,\"3\",0,1,1,\"Lineowave Technologies"\n')
  #ser.write(b'TEXT 120,100,\"2\",0,1,1,\"Line12342353512141hfckahkjf\"\n')
  temp = "TEXT 55,170,\"3\",0,1,1,\"Date: " +Data[0]     + "    WT B/f Cycle:  " + Data[5]    +"  KG\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 55,220,\"3\",0,1,1,\"Start Time: " +Data[2]     + "   WT A/f Cycle:  " + Data[6]    +"  KG\"\n"
  ser.write(temp.encode("utf-8"))
  #ser.write(b'TEXT 65,275,\"3\",0,1,1,\"Starting Time :             Device :       \"\n')
  temp = "TEXT 55,270,\"3\",0,1,1,\"Process No: " + Data[1]  + "   End Time : " + Data[4] + "\"\n"
  ser.write(temp.encode("utf-8"))
  ser.write(b'PRINT 1\n')
  
  ser.write(b'SIZE 100 mm, 50 mm\n')
  ser.write(b'GAP 3 mm, 0 mm\n')
  ser.write(b'DIRECTION 1\n');
  ser.write(b'CLS\n')
  ser.write(b'TEXT 100,30,\"4\",0,1,1,\"    Cycle Information\"\n')
  ser.write(b'TEXT 250,75,\"2\",0,1,1,\"Lineowave Technologies"\n')
  temp = "TEXT 65,120,\"2\",0,1,1,\"Data : " +Data[2]     + "            Weight :  " + Data[10]    +"   min\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,150,\"2\",0,1,1,\"Start Time  : " +Data[6]+ "  KG"  + "    Start Hold Time :  " + Data[5]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,180,\"2\",0,1,1,\"End Time : " +Data[3]     + "       Total Time :  " + Data[5]    +"   min\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,210,\"2\",0,1,1,\"Start Temp  : " +Data[1]     + "   Temp Max :  " + Data[8]    +"\"\n"
  ser.write(temp.encode("utf-8"))
  temp = "TEXT 65,240,\"2\",0,1,1,\"Start : " +Data[4]     + "               Prcocess No :" + Data[9]    +"    \"\n"
  ser.write(temp.encode("utf-8"))
  ser.write(b'TEXT 100,300,\"4\",0,1,1,\"    Disinfected !\"\n')
  
  ser.write(b'PRINT 1\n')
  """
  j = 0
  while j < 9:
    #ser
    print(Data[j].encode("utf-8"))
    j += 1
            
    #ser.write(j.encode("utf-8"))
  #ser.write(Data.encode("utf-8"))
  #ser.write(b'PRINT 1\n')"""

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
#ser.open()
#ser1.open()

while True:
  if ser1.in_waiting:
    Test = ser1.readline()
    print(Test)
    #print(type(Test))
    ser1.flushInput()
    ser1.flushOutput()
    string = (Test.decode("utf-8")).rstrip().lstrip()
    #string1 = string
    Data = string.split("#")
    #print(Data)
    
    #Data =  "TEXT 10,30,\"3\",0,1,1,\"" + string1 + "\"\n" 
    printer_test(ser,Data)
    #i+=1
#Data =  b'TEXT 10,30,\"3\",0,1,1,\"' + Test +'\"\n' 





