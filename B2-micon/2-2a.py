from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)

pinLED = machine.Pin(26, mode=machine.Pin.OUT)
while True:
  pinLED.value(1)
  wait(1)
  pinLED.value(0)
  wait(1)