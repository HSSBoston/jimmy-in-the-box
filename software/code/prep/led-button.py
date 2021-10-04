import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Start writing your program below

buttonVcc = 19
buttonSwitch = 26

GPIO.setup(buttonVcc, GPIO.OUT)
GPIO.setup(buttonSwitch, GPIO.IN)

GPIO.output(buttonVcc, GPIO.HIGH)

while True:
    try:
        if GPIO.input(buttonSwitch) == GPIO.LOW:
            print("Pushed!")
            time.sleep(2)
    except:
        break

# GPIO.output(26, GPIO.LOW)

# Write your program above this line
GPIO.cleanup()