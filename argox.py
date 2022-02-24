import serial
from time import sleep

ser = serial.Serial(
    port="COM7",
    baudrate=9600,
    timeout=0.05
)

serP = serial.Serial(
    port="COM31",
    baudrate=9600,
    timeout=0.05
)


while True:
    data = ser.readline()
    strData = str(data)
    strData = strData.replace('\\r\\n', "")
    strData = strData.replace('GS', "")
    strData = strData.replace('G', "")
    strData = strData.replace('\'', "")
    strData = strData.replace('+', "")
    strData = strData.replace('b', "")
    strData = strData.replace(' ', "")


    # print(data)
    if strData != '':
        fltData = float(strData)
        print(strData, fltData)

        if fltData >= 1000.00:
            value = strData
            gabung = 'A50,190,0,4,2,2,N,"' + value + '"\r\n'
            unit = 'A290,190,0,4,2,2,N,"g"\r\n'
            datePrint = 'A30,40,0,4,1,1,N,TDyy-me-dd\r\n'
            timePrint = 'A250,40,0,4,1,1,N,TTh:m:s\r\n'

            serP.write(unit.encode())
            serP.write(gabung.encode())
            serP.write(timePrint.encode())
            serP.write(datePrint.encode())
            serP.write('P1\r\n'.encode())
        else:
            value = strData
            gabung = 'A80,190,0,4,2,2,N,"' + value + '"\r\n'
            unit = 'A290,190,0,4,2,2,N,"g"\r\n'
            datePrint = 'A30,40,0,4,1,1,N,TDyy-me-dd\r\n'
            timePrint = 'A250,40,0,4,1,1,N,TTh:m:s\r\n'

            serP.write(unit.encode())
            serP.write(gabung.encode())
            serP.write(timePrint.encode())
            serP.write(datePrint.encode())
            serP.write('P1\r\n'.encode())
    sleep(1)
