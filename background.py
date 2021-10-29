'''
Created on 2018

@author: programmer
'''
import ctypes

'''tsclibrary = ctypes.WinDLL("c:\\64\\TSCLIB.dll");'''
tsclibrary = ctypes.WinDLL("C:\\Users\\AGV\\Downloads\\TSC_Python_SDK_Example\\tsc_sample\\libs\\TSCLIB.dll");

if __name__ == '__main__':
    pass
a_str = "HELLO WORLD";
print(a_str);



'''
tsclibrary.about();
'''
tsclibrary.openportW("COM3");
'''
tsclibrary.openportW("USB");
'''
#// AUTODETECT
tsclibrary.sendcommandW("SIZE 100 mm, 50 mm"); #// size of label width mm, height mm - 100 x 50
tsclibrary.sendcommandW("GAP 3 mm, 0 mm");
tsclibrary.sendcommandW("DIRECTION 1");
tsclibrary.sendcommandW("CLS");
tsclibrary.sendcommandW("TEXT 10,30,\"3\",0,1,1,\"123456\"");
#tsclibrary.barcodeW("10","150","EAN13","80","1","0","2","4","123456789012");
#tsclibrary.printerfontW("10", "70", "4", "0", "1", "1", "TEST PRINTOUT");
#tsclibrary.windowsfontW("10","100","24","0", "0", "0", "Arial","Window Font Test");
#tsclibrary.downloadpcxW("UL.PCX","UL.PCX");
#tsclibrary.sendcommandW("PUTPCX 10,300,\"UL.PCX\"");
#tsclibrary.printlabelW("1","1");
tsclibrary.closeport();




