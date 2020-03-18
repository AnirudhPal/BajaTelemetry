# BajaTelemetry

I am putting together a user-guide to make sure you guys can set this up yourself whenever necessary.

## Setup

This step assumes that something is broken and you want to setup from scratch. You will need the following hardware:

* Android/iOS Phone (Android is Better)
* Raspberry Pi
* SD Card
* Laptop with SD Card Reader
* Keyboard
* Monitor with HDMI

### Download OS and Flash

Follow the instructions in the installation guide and install the Raspbian Lite OS on the SD card. The OS image can be found in the link below:

* Click the Installation Guide Link below.
* Follow the few lines under Using Raspberry Pi Imager.
* Click the first link on that site and download the imager for your operating system; example: Rapsberry Pi Imager for Windows.
* Then click on the OS Image link below and download Raspbian Lite.
* Follow the remaining instructions to write to the SD card. 

[Installation Guide](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

[OS Image](https://www.raspberrypi.org/downloads/raspbian/)

### Setup Raspberry Pi, Laptop and Phone

* Set phone to enable hotpsot. 
* Have a fixed password. 
* Connect the laptop to that hotspot. **Minimize Data Usage**. 
* Connect the Pi to that hotpsot. The Pi should auto connect after boot once this is done.
   * Put SD Card into the Pi.
   * Connect monitor & keyboard to the Pi.
   * Connect power.
   * Wait for OS to boot.
   * Login using user id & password. 
   * Use terminal to connect to hotspot using instructions [here](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).
   * To check internet connection type: 
   `ping google.com`
   * If the packets lost is less than 100% this means that you are connected to the wifi.
* Enable SSH on Pi

![](https://github.com/AnirudhPal/BajaTelemetry/blob/master/Images/1.PNG?raw=true)
* Similarly enable I2C on Pi

### SSH into the Pi

* Open PowerShell(Windows) or Terminal(Mac/Linux) on laptop.
* On the Pi enter. `hostname -I`
* Take note of the IP. The IP stays the same till the Pi is connected and doesn't reboot. Usually when it reboots, it ends up with the same IP once it connects.
* On the laptor enter. `ssh pi@<IP>`
* Say yes to whatever it asks and enter password.


