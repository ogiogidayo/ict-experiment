from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x000000)
pir_0 = unit.get(unit.PIR, unit.PORTA)
label1 = M5TextBox(147, 112, "PIR", lcd.FONT_Default, 0xffffff, rotate=0)


while True:
  label1.setText(str(pir_0.state))