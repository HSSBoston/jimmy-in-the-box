import kintone, os, time, gpsserial as gps
from kintone import getCurrentTimeStamp
from geopy.geocoders import Nominatim

serialPort = "/dev/serial0"
appName = "jwst-demo-panda"

sdomain = "hssboston"
appId = "6"
token = "emmH0XsElPiRsBDNyqJnYjb5sXIMcmhEIYM3GH2D"

gpsSerialPort = gps.init(serialPort)
geolocator = Nominatim(user_agent=appName)

while True:
    try:
        timeStamp = getCurrentTimeStamp()
        picFile = "pic/" + timeStamp + ".jpg"
        command = "raspistill -t 500 -rot 180 -w 800 -h 600 -o " + picFile

        status = os.system(command)
        if(status==0):
            print(timeStamp, end=" ")
            print("Photo captured.")
        else:
            print("Failed to capture a picture")

        fileKey = kintone.uploadFile(subDomain=sdomain,
                                     apiToken=token,
                                     filePath=picFile)
        if fileKey is None:
            print("Failed to upload a picture file to Kintone (file key: None).")

        gpsData = gps.getData(gpsSerialPort)
        print(gpsData)

        decimalLat = gps.getDecimalLatitude(gpsData)
        decimalLon = gps.getDecimalLongitude(gpsData)
        gMapsLink = "https://www.google.com/maps?q=" + str(decimalLat) + "," + str(decimalLon)
        print("Decimal latitude: " + str(decimalLat) + ", Decimal longitude: " + str(decimalLon))
                
        location = geolocator.reverse( query=(decimalLat, decimalLon) )
        locationDataset = location.raw
        address = locationDataset["address"]
        if "city" in address:
            cityTown = address["city"]
        if "town" in address:
            cityTown = address["town"]
        state = address["state"]
        print("Address: " + cityTown + ", " + state)
        
        gpsData = gps.getGgaData(gpsSerialPort)
        print(gpsData)
        elevation = gps.getElevation(gpsData)
        print("Elevation (m): " + elevation)

        payload = {"app": appId,
                   "record": {"photo": {"value": [{"fileKey": fileKey}]},
                              "lat": {"value": decimalLat},
                              "lon": {"value": decimalLon},
                              "elevM": {"value": elevation},
                              "cityTown" : {"value": cityTown},
                              "state" : {"value": state},
                              "link" : {"value": gMapsLink} }}

        recordId = kintone.uploadRecord(subDomain=sdomain,
                                        apiToken=token,
                                        record=payload)
        if recordId is None:
            print("Failed to upload a photo and the current location info to Kintone (record ID: None).")

        print("")
        time.sleep(30)
    except KeyboardInterrupt:
        break
gpsSerialPort.close()
