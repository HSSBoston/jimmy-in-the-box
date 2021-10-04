import sys, serial

delete_two_bytes=False
if sys.version_info[0]==3:
    delete_two_bytes=True

serialPort = "/dev/serial0"
gpsSerialPort = serial.Serial(serialPort, baudrate = 9600, timeout = 0.5)

while True:
    try:
        nmeaSentence = (str)(gpsSerialPort.readline())
        if delete_two_bytes:
            nmeaSentence = nmeaSentence[2:]
        nmeaDataType = nmeaSentence[3:6]
        if nmeaDataType == "RMC" or nmeaDataType == "GGA":
            print(nmeaSentence)
        

    except KeyboardInterrupt:
        break
gpsSerialPort.close()
