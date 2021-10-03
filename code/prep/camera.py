import os, sys, kintone, time
from kintone import getCurrentTimeStamp
# Write your program below

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
