import gpsserial as gps
from geopy.geocoders import Nominatim
import kintone, time

serialPort = "/dev/serial0"
appName = "jwst-demo-panda"

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

gpsSerialPort = gps.init(serialPort)
geolocator = Nominatim(user_agent=appName)

while True:
    try:
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
        print("Address: " + cityTown + ", " + ", " + state)

        payload = {"app": appId,
                   "record": {"lat": {"value": decimalLat},
                              "lon": {"value": decimalLon},
                              "cityTown" : {"value": cityTown},
                              "state" : {"value": state},
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
