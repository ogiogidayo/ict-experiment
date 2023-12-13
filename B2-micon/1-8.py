from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit


setScreenColor(0x000000)
color_0 = unit.get(unit.COLOR, unit.PORTA)


color = None

label0 = M5TextBox(123, 91, "明るさ", lcd.FONT_UNICODE, 0xffffff, rotate=0)
label1 = M5TextBox(53, 148, "RED", lcd.FONT_Default, 0xff0000, rotate=0)
label2 = M5TextBox(132, 148, "GREEN", lcd.FONT_Default, 0x6eff00, rotate=0)
label3 = M5TextBox(226, 148, "BLUE", lcd.FONT_Default, 0x1900ff, rotate=0)


while True:
  color = color_0.rawData
  label0.setText(str(color[0]))
  label1.setText(str(color[1]))
  label2.setText(str(color[2]))
  label3.setText(str(color[3]))
  wait(1)