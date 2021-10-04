import RPi.GPIO as GPIO
import os, sys, kintone, time
from kintone import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Start writing your program below

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

button = 19
buttonSwitch = 26

GPIO.setup(button, GPIO.OUT)
GPIO.setup(buttonSwitch, GPIO.IN)

GPIO.output(button, GPIO.HIGH)

while True:
    try:
        if GPIO.input(buttonSwitch) == GPIO.LOW:
            print("Button Pushed!", end=" ")

            timeStamp = getCurrentTimeStamp()
            picFile = "pic/" + timeStamp + ".jpg"
            command = "raspistill -t 500 -w 800 -h 600 -o " + picFile

            status = os.system(command)
            if(status==0):
                print(timeStamp, end=" ")
                print("Photo captured.")
            else:
                print("Failed to capture a picture")
                sys.exit()

            fileKey = kintone.uploadFile(subDomain=sdomain,
                                         apiToken=token,
                                         filePath=picFile)
            if fileKey is None:
                sys.exit()

            memo = "Hi from Raspi!"
            payload = {"app": appId,
                       "record": {"photo": {"value": [{"fileKey": fileKey}] },
                                  "memo": {"value": memo} }}

            recordId = kintone.uploadRecord(subDomain=sdomain,
                                            apiToken=token,
                                            record=payload)
            if recordId is None:
                sys.exit()
#            time.sleep(2)
    except:
        break

# Write your program above this line
GPIO.cleanup()