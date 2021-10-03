import gpsserial as gps

serialPort = "/dev/serial0"
gpsSerialPort = gps.init(serialPort)
    
while True:
    try:
        gpsData = gps.getData(gpsSerialPort)
        print(gpsData)

        lat = gps.getLatitude(gpsData)
        lon = gps.getLongitude(gpsData)
        print("Raw latitude: " + lat + ", Raw longitude: " + lon)

        nsIndicator = gps.getNSIndicator(gpsData)
        ewIndicator = gps.getEWIndicator(gpsData)
        
        latDegree = gps.getLatitudeDegree(gpsData)
        latMinute = gps.getLatitudeMinute(gpsData)
        lonDegree = gps.getLongitudeDegree(gpsData)
        lonMinute = gps.getLongitudeMinute(gpsData)
        print("Latitude degree: " + str(latDegree) +
              ", Latitude minute: " + str(latMinute) + ", NS Indicator: " + nsIndicator)
        print("Longitude degree: " + str(lonDegree) +
              ", Longitude minute: " + str(lonMinute) + ", EW Indicator: " + ewIndicator)
        
        decimalLat = gps.getDecimalLatitude(gpsData)
        decimalLon = gps.getDecimalLongitude(gpsData)
        print("Decimal latitude: " + str(decimalLat) + ", Decimal longtitude: " + str(decimalLon))

        gMapsLink = "https://www.google.com/maps?q=" + str(decimalLat) + "," + str(decimalLon)
        print("Google Maps link: " + gMapsLink)
        
        print("")
    except KeyboardInterrupt:
        break
gpsSerialPort.close()
