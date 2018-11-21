import serial
from serial import Serial
forchar = 0
idcom = []

ser = serial.Serial(
    port = 'COM15',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=None)

print("connected to: " + ser.portstr)
count=1

while True:
    print(ser.readline())
    # for line in ser.readline():
    #     forchar = forchar + 1
    #     idcom.append(line)
    #     print(line )
    # if forchar >= 113:
    #     break

'''
while True:
        while ser.inWaiting() == 0:
            pass
        #необходимая работа с данными...
        '''