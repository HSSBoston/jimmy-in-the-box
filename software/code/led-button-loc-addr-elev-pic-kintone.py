import RPi.GPIO as GPIO, gpsserial as gps
import os, sys, kintone, time
from kintone import getCurrentTimeStamp
from geopy.geocoders import Nominatim

GPIO.setmode(GPIO.BCM)
# Start writing your program below

serialPort = "/dev/serial0"
appName = "jwst-demo-panda"

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

button = 19
buttonSwitch = 26

GPIO.setup(button, GPIO.OUT)
GPIO.setup(buttonSwitch, GPIO.IN)

GPIO.output(button, GPIO.HIGH)

gpsSerialPort = gps.init(serialPort)
geolocator = Nominatim(user_agent=appName)

while True:
    try:
        if GPIO.input(buttonSwitch) == GPIO.LOW:
            print("Button Pushed!", end=" ")

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
            print("HERE")
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
    except:
        break

# Write your program above this line
GPIO.cleanup()