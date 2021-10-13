# Software

## Required Software

- The most recent version of Raspi OS
- Python 3

## Changing Raspi OS Configuration

In Raspi OS Configuration, enable Camera and Serial Port, and disable Serial Console:

<p align="center">
  <img src="../images/raspios.jpg" width="350" />
</p>

Reboot your Raspi OS.

## Using a Camera

To check if your camera works properly, run the following command in Terminal:

```
raspistill -o test.jpg
```

Your Raspi places a picture file (test.jpg) at the current folder. If you want to store a picture file at your Pictures folder, run this command:

```
raspistill -o ~/Pictures/test.jpg
```

## Using a GPS Receiver

To check if your GPS receiver works properly, run the following command in Terminal:

```
sudo stty -F /dev/serial0 9600 raw

```

Note that “0” of “serial0” is ZERO, not “O”. Then, run one more command :

```
cat /dev/serial0
```

Most likely, you will get something like this.

<p align="center">
  <img src="../images/terminal-serial.jpg" width="400" />
</p>

All the commas and 99.99 mean that your GPS receiver has not yet calculated its position. Keep running the “cat” command. If in 10 minutes it still looks like this, you need to move the antenna closer to a window.

When the calculation is successful, the text will change like this.

<p align="center">
  <img src="../images/terminal-serial2.jpg" width="500" />
</p>

Look at a line starting with $GPRMC or $GNRMC.

- 4219.82563 is latitude.
- N means North.
- 07106.86235 is longitude.
- W means West.

## Making a Kintone App

## Making and Running Python Apps
