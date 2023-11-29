from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x000000)
dual_button_1 = unit.get(unit.DUAL_BUTTON, unit.PORTA)
label1 = M5TextBox(147, 112, "PIR", lcd.FONT_Default, 0xffffff, rotate=0)

def btnBlue1_wasPressed():
  label1.setText('Touched')
  pass
dual_button_1.btnBlue.wasPressed(btnBlue1_wasPressed)