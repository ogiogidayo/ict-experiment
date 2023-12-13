from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x000000)
tof_0 = unit.get(unit.TOF, unit.PORTA)

label0 = M5TextBox(133, 103, "distance", lcd.FONT_UNICODE, 0x03cdff, rotate=0)

while True:
  label0.setText(str(tof_0.distance))