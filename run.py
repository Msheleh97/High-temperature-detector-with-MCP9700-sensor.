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
