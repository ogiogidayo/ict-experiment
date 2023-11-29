from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit


setScreenColor(0x000000)
neopixel_0 = unit.get(unit.NEOPIXEL, unit.PORTB, 15)

while True:
  neopixel_0.setColorFrom(1, 15, 0xff0000)
  neopixel_0.show()
  wait(1)
  neopixel_0.setColorAll(0x3333ff)
  neopixel_0.show()
  wait(1)
  neopixel_0.setColorAll(0x009900)
  neopixel_0.show()
  wait(1)
  neopixel_0.setColorAll(0xffff00)
  neopixel_0.show()
  wait(1)
  neopixel_0.setColorAll(0xff9966)
  neopixel_0.show()
  wait(1)
  neopixel_0.setColorAll(0xcc33cc)
  neopixel_0.show()
  wait(1)