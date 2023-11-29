from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x000000)
env2_0 = unit.get(unit.ENV2, unit.PORTA)
label1 = M5TextBox(53, 148, "気温", lcd.FONT_Default, 0xff0000, rotate=0)
label2 = M5TextBox(132, 148, "湿度", lcd.FONT_Default, 0x6eff00, rotate=0)
label3 = M5TextBox(226, 148, "気圧", lcd.FONT_Default, 0x1900ff, rotate=0)


while True:
  label1.setText(str(env2_0.temperature))
  label2.setText(str(env2_0.humidity))
  label3.setText(str(env2_0.pressure))