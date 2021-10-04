import gpsserial as gps
import kintone, time

serialPort = "/dev/serial0"

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

gpsSerialPort = gps.init(serialPort)
    
while True:
    try:
        gpsData = gps.getData(gpsSerialPort)
        print(gpsData)

        decimalLat = gps.getDecimalLatitude(gpsData)
        decimalLon = gps.getDecimalLongitude(gpsData)
        print("Decimal latitude: " + str(decimalLat) + ", Decimal longitude: " + str(decimalLon))
        
        gMapsLink = "https://www.google.com/maps?q=" + str(decimalLat) + "," + str(decimalLon)
        print("Google Maps link: " + gMapsLink)

        payload = {"app": appId,
                   "record": {"lat": {"value": decimalLat},
                              "lon": {"value": decimalLon},
                              "link" : {"value": gMapsLink} }}

        recordId = kintone.uploadRecord(subDomain=sdomain,
                                        apiToken=token,
                                        record=payload)
        if recordId is None:
            print("Failed to upload the current location info to Kintone")

        print("")
        time.sleep(30)
    except KeyboardInterrupt:
        break
gpsSerialPort.close()
