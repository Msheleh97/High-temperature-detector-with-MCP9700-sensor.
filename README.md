
# High temperature detector with MCP9700 sensor.
---
> Mohammad Mshaleh (mm224ez)
---
This project is about a high temperature detector that uses a lopy4 device and a MCP9700 sensor. The lopy4 device will be programmed to use an app to send a notification to warn the user if the temperature is high.This project can be used as a fire alarm and also can be used to control a room temperature.

![](https://i.imgur.com/3DoX2xe.jpg)




# Purpose
These tutorials will give you an idea on how the internet of things (IoT) works. This device can be used as a thermometer and it can be programmed depending on the use situation. This project can also be developed to a more advanced thermometer and it can be coupled to more sensors to perform a more specific job.


# Materials
To create an identical project you will need to buy some Materials. All materials I needed came with a LoPy4 and sensor bundle kit and the price of it is 949 SEK. The kit contains a lopy4 device, expansion board, led , resistors and sensors. For more information visit this [webbsite].


The materials you will need is:
- LoPy4 with headers: is a micropython IoT platform. 
- Expansion board: used to connect the loPy4 to the wires.
- Jumper wire: to connect the expansion board with the breadboard.
- Antennae: for better Wifi signal.
- Micro USB cable: to power the expansion board and the loPy4.
- MCP9700 sensor: temperature sensor.
- Breadboard: the board that connects the sensor with the wires.

[webbsite]: https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/

# IDE setup
The first thing you will need to do is to download an IDE to program the device. The IDE i used is Visual Studio Code, to download VS code follow this [tutorial].

After downloading VS code you will need to download a plugin that will help you to run and upload the code on the loPy4. To download the plugin start the VS code go to extensions and type pymakr and download it and now you are ready to start programming.

[tutorial]:https://code.visualstudio.com/docs/setup/setup-overview

# Putting the hardware pieces together
First step will be connecting the expatitions board together with the breadboard and the sensor. Be sure to connect the yellow wire to GND, orange to 3v3 and red to P16. The sensor can be placed wherever on the breadboard but the wires must be connected as the picture below shows.
![](https://i.imgur.com/B350GvN.jpg)

The final step is to connect the antennae with the loPy4 as in the picture below. Make note that the project does not need the antennae but i used it to receive a better Wifi signal.
 
![](https://i.imgur.com/5OEPgwt.jpg)
# Internet connection
The loPy4 must be connected to the internet network to send the data from the sensor. With the loPy4 device you can be connected to the internet via Wifi, Sigfox, LoRa. Sigfox and LoRa can be used if you place the device in a farm or a cottage that does not have a Wifi network or far away from it. But in my use case it will be fine to connect it to the Wifi because it will be used in my home which has a Wifi network.

# Dashboard
After connecting all hardware together and connecting the loPy4 to the computer, you will need a dashboard that represents our data sent by the loPy4. 
I used pybytes to represent the data and it can also be used as a database. 
![](https://i.imgur.com/nlZwDua.png)

# Sending a phone notification
When the room temperature gets too high you will need to receive a warning. A phone notification can be used as one. To get notification you will need a webrequest and to do this you will need to use the IFTTT. You will need to follow this [IFTTT] setup tutorials. Finally you will need to download the IFTTT app on your phone device.

![](https://i.imgur.com/WxZpv2O.jpg)

[IFTTT]: https://community.progress.com/s/article/How-to-create-the-IFTTT-action

# The code 
The code I used in this project is written below. I have also commented on the code for a better understanding of it.
```python=
#Author: Mohammad Mshaleh
#The libraries that will be used in this program.
import machine
import time
import pycom 
import urequests
from network import WLAN

#Check if the lopy4 is connected to the internet.
wlan = WLAN()
if wlan.isconnected():
  print("The device is connected to the internet")
else:
  print("The device is not connected to the internet")

#Make a url request.
phonenotification = "https://maker.ifttt.com/trigger/Event1/with/key/d-FPf2Itm-iYJ8XyTQBg8t"

adc = machine.ADC()
apin = adc.channel(pin='P16')

while True:

  #Reading data from the sensor.
  mv = apin.voltage()
  temperature = (mv - 500.0) / 10.0

  #If the tempeture is higher than or equel to 50 °C a notification will be send to the mobile phone. 
  if temperature >= 50:
    print("The current temperature is high: " , temperature)
    req = urequests.post(url=phonenotification, json={'value1': temperature})
    time.sleep(20)

  #If the temperture is lower that 50 °C the temp will be printed in the terminal each 20 second.
  else:
    print("The current temperature is : " , temperature)
    pybytes.send_signal(1,temperature)
    time.sleep(20)



