import gpsserial as gps

serialPort = "/dev/serial0"
gpsSerialPort = gps.init(serialPort)
    
while True:
    try:
        gpsData = gps.getData(gpsSerialPort)
        print(gpsData)
        
        decimalLat = gps.getDecimalLatitude(gpsData)
        decimalLon = gps.getDecimalLongitude(gpsData)
        print("Decimal latitude: " + str(decimalLat) + ", Decimal longtitude: " + str(decimalLon))

        gMapsLink = "https://www.google.com/maps?q=" + str(decimalLat) + "," + str(decimalLon)
        print("Google Maps link: " + gMapsLink)
        
        print("")
    except KeyboardInterrupt:
        break
gpsSerialPort.close()
