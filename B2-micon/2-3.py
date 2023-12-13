from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)

pinRedLED = machine.Pin(5, mode=machine.Pin.OUT)
pinGreenLED = machine.Pin(26, mode=machine.Pin.OUT)
while True:
  pinRedLED.value(1)
  pinGreenLED.value(0)
  wait(0.5)
  pinRedLED.value(0)
  pinGreenLED.value(1)
  wait(0.5)
  pinRedLED.value(1)
  wait(0.5)
  pinRedLED.value(0)
  pinGreenLED.value(0)
  wait(0.5)