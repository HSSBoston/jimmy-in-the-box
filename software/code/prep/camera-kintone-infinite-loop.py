import os, sys, kintone, time
from kintone import getCurrentTimeStamp
# Write your program below

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

interval = 10

while True: 
    try:
        timeStamp = getCurrentTimeStamp()
        picFile = timeStamp + ".jpg"
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
        time.sleep(interval)
    except KeyboardInterrupt:
        break

