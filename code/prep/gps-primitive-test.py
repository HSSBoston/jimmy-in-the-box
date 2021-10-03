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
        
#         gpsData = gps.getData(gpsSerialPort)
#         print(gpsData)
# 
#         lat = gps.getLatitude(gpsData)
#         lon = gps.getLongitude(gpsData)
#         print("Raw latitude: " + lat + ", Raw longitude: " + lon)
# 
#         nsIndicator = gps.getNSIndicator(gpsData)
#         ewIndicator = gps.getEWIndicator(gpsData)
#         
#         latDegree = gps.getLatitudeDegree(gpsData)
#         latMinute = gps.getLatitudeMinute(gpsData)
#         lonDegree = gps.getLongitudeDegree(gpsData)
#         lonMinute = gps.getLongitudeMinute(gpsData)
#         print("Latitude degree: " + str(latDegree) +
#               ", Latitude minute: " + str(latMinute) + ", NS Indicator: " + nsIndicator)
#         print("Longitude degree: " + str(lonDegree) +
#               ", Longitude minute: " + str(lonMinute) + ", EW Indicator: " + ewIndicator)
#         
#         decimalLat = gps.getDecimalLatitude(gpsData)
#         decimalLon = gps.getDecimalLongitude(gpsData)
#         print("Decimal latitude: " + str(decimalLat) + ", Decimal longtitude: " + str(decimalLon))
# 
#         gMapsLink = "https://www.google.com/maps?q=" + str(decimalLat) + "," + str(decimalLon)
#         print("Google Maps link: " + gMapsLink)
#         
#         print("")
    except KeyboardInterrupt:
        break
gpsSerialPort.close()
