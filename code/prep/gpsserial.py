# Library to read GPS data (NMEA sentences)
# Sept 29, 2021 v0.02
# Jun Suzuki (https://github.com/jxsboston)
# Igor Golger
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/

import serial, sys

#we need the python version
delete_two_bytes=False
if sys.version_info[0]==3:
    delete_two_bytes=True

def init(serialPort):
    gpsSerialPort = serial.Serial(serialPort, baudrate = 9600, timeout = 0.5)
    return gpsSerialPort

# Captures and returns RMC data, which has time, date, position, course and speed data.
#
def getData(gpsSerialPort):
    while True:
        try:
            nmeaSentence = (str)(gpsSerialPort.readline())
            # Python3 returns the string starting with 'b, which is to be removed here.
            if delete_two_bytes:
                nmeaSentence = nmeaSentence[2:]
            if isRmcSentence(nmeaSentence):
                return nmeaSentence
            else:
                continue
        except KeyboardInterrupt:
            gpsSerialPort.close()
            sys.exit()

def getGgaData(gpsSerialPort):
    while True:
        try:
            nmeaSentence = (str)(gpsSerialPort.readline())
            # Python3 returns the string starting with 'b, which is to be removed here.
            if delete_two_bytes:
                nmeaSentence = nmeaSentence[2:]
            if isGgaSentence(nmeaSentence):
                return nmeaSentence
            else:
                continue
        except KeyboardInterrupt:
            gpsSerialPort.close()
            sys.exit()
            
def isRmcSentence(nmeaSentence):
    nmeaDataType = nmeaSentence[3:6]
    if nmeaDataType == "RMC":
        return True

def isGgaSentence(nmeaSentence):
    nmeaDataType = nmeaSentence[3:6]
    if nmeaDataType == "GGA":
        return True
    
def isValid(nmeaSentence):
    sentenceParts = nmeaSentence.split(",")
    if isRmcSentence(nmeaSentence) and sentenceParts[2] != "V":
        return True
    else:
        return False    

# Returns latitude in string based on the raw format (ddmm.mmmmm)
#
def getLatitude(nmeaSentence):
    if isValid(nmeaSentence):
        sentenceParts = nmeaSentence.split(",")
        latitude = sentenceParts[3]
        return latitude
    else:
        return None

# Returns longitude in string based on the raw format (dddmm.mmmmm)
#
def getLongitude(nmeaSentence):
    if isValid(nmeaSentence):
        sentenceParts = nmeaSentence.split(",")
        longitude = sentenceParts[5]
        return longitude
    else:
        return None

def getNSIndicator(nmeaSentence):
    if isValid(nmeaSentence):
        sentenceParts = nmeaSentence.split(",")
        nsIndicator = sentenceParts[4]
        return nsIndicator
    else:
        return None

def getEWIndicator(nmeaSentence):
    if isValid(nmeaSentence):
        sentenceParts = nmeaSentence.split(",")
        ewIndicator = sentenceParts[6]
        return ewIndicator
    else:
        return None        

def getLatitudeDegree(nmeaSentence):
    rawLatitude = getLatitude(nmeaSentence)
    if rawLatitude is None:
        return None
    else:
        return float(rawLatitude[0:2])
    
def getLatitudeMinute(nmeaSentence):
    rawLatitude = getLatitude(nmeaSentence)
    if rawLatitude is None:
        return None
    else:
        return float(rawLatitude[2:len(rawLatitude)])

def getLongitudeDegree(nmeaSentence):
    rawLongitude = getLongitude(nmeaSentence)
    if rawLongitude is None:
        return None
    else:
        return float(rawLongitude[0:3])
    
def getLongitudeMinute(nmeaSentence):
    rawLongitude = getLongitude(nmeaSentence)
    if rawLongitude is None:
        return None
    else:
        return float(rawLongitude[3:len(rawLongitude)])

def getDecimalLatitude(nmeaSentence):
    latDegree = getLatitudeDegree(nmeaSentence)
    latMinute = getLatitudeMinute(nmeaSentence)
    if latDegree is None or latMinute is None:
        return None
    else:
        decimalLat = latDegree + latMinute/60.0
        if getNSIndicator(nmeaSentence)=="S":
            decimalLat = -decimalLat
        return decimalLat

def getDecimalLongitude(nmeaSentence):
    lonDegree = getLongitudeDegree(nmeaSentence)
    lonMinute = getLongitudeMinute(nmeaSentence)
    if lonDegree is None or lonMinute is None:
        return None
    else:
        decimalLon = lonDegree + lonMinute/60.0
        if getEWIndicator(nmeaSentence)=="W":
            decimalLon = -decimalLon
        return decimalLon

def getElevation(nmeaSentence):
    if isGgaSentence(nmeaSentence):
        sentenceParts = nmeaSentence.split(",")
        elevation = sentenceParts[9]
        return elevation
    else:
        return None


