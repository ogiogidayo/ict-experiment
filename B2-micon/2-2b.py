# 点灯速度変更
from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)

pinLED = machine.Pin(26, mode=machine.Pin.OUT)
while True:
  pinLED.value(1)
  wait(0.2)
  pinLED.value(0)
  wait(0.2)