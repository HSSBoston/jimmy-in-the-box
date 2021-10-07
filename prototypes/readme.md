# Telescope Model Prototypes

We made 3 prototypes in this project.

## Prototype 1

<p align="center">
  <img src="../images/prototype1-1.jpg" height="360" />
  <img src="../images/prototype1-2.jpg" width="300" />
</p>
<p align="center">
  <img src="../images/prototype1-3.jpg" width="300" />
  <img src="../images/prototype1-4.jpg" width="300" />  
</p>

This prototype models JWST's primary mirror with a hexagonal origami tessellation. The tessellation is folded from a piece of paper. See [this page](../origami/) for more details about the tessellation.

This prototype also models JWST's [Secondary Mirror Support Structure (SMSS)](https://news.northropgrumman.com/news/features/nasas-james-webb-space-telescope-secondary-mirror-deploys-for-the-first-time-using-the-spacecraft-flight-electronics), which uses 3 arms to deploy the secondary mirror. The arms are modeled with bamboo skewers, which are attached to the primary mirror with two hinges made with paper tape and plastic straws. Just like JWST's arms, our arms fold toward the primary mirror (so that they can reduce their volume and can be placed in a rocket) and unfold to form a tripod (so that the secondary mirror can stay at a distance from the primary mirror).

JWST's sun shield is modeled with sheet protectors. Five layers of them are connected with foundation bars with strings. They can fold and unfold horizontally.



## Prototype 2

<p align="center">
  <img src="../images/prototype2.jpg" width="500" />
</p>

This prototype models JWST's primary mirror and sunshield. The primary mirror is modeled with a hexagonal origami tessellation, just like in our prototype 1. The sunshield is also modeled with origami crafts. We folded a long (silver) hexagon from a piece of paper, stacked five of them and placed them under the primary mirror. See [this page]((../origami/)) to learn how to fold them.

This prototype is equipped with a Raspberry Pi computer, camera and GPS receiver. The camera is attached to the middle of the primary mirror (in a black hexagon). We wrote a [Python program](../software/code/gps-loc-addr-pic-kintone.py) to periodically take a picture with the camera and measure its current location (latitude and longitude) with a GPS receiver. The program also uploads the picture and location information to a cloud database called [Kintone](https://developer.kintone.io/).

## Prototype 3

This prototype models JWST's primary mirror and sunshield with origami crafts as our prototypes 1 and 2 do. They are attached to two snake cubes, which model JWST's vertical tower and bottom foundation bars. Bottom foundation bars fold and unfold just like in JWST.

This prototype is equipped with a Raspberry Pi computer, camera, push button and GPS receiver. It places the camera at the middle of the primary mirror, as our prototype 2 does. It is connected with a Raspberry Pi in a case, which is attached to the vertical tower as JWST's [Integrated Science Instrument Module (ISIM)](https://www.jwst.nasa.gov/content/observatory/instruments/index.html) is attached to the tower. A push button and GPS receiver are also attached to the tower and connected to the Raspberry Pi.

We wrote a [Python program](gps-loc-addr-elev-pic-kintone.py) for the Raspberry Pi to periodically take a picture with a camera and measure its current position (latitude, longitude and elevation) with a GPS receiver. The program converts a pair of latitude and longitude to an address (town and state) with a reverse-geocoding service called [Nominatim](https://nominatim.org/). It periodically uploads a picture, position information and address to [Kintone](https://developer.kintone.io/). We also wrote [another Python program](../software/code/led-button-loc-addr-elev-pic-kintone.py) to detect a push button is pressed, take a picture and upload it to [Kintone](https://developer.kintone.io/).  




<p align="center">
  <img src="../images/prototype3-1.jpg" width="250" />
  <img src="../images/prototype3-2.jpg" width="250" />
  <img src="../images/prototype3-3.jpg" height="35e0" />
</p>
<p align="center">
  <img src="../images/prototype3-4.jpg" width="250" />
  <img src="../images/prototype3-5.jpg" width="500" />
</p>
