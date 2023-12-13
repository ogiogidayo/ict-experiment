from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x000000)
dual_button_0 = unit.get(unit.DUAL_BUTTON, unit.PORTB)

label0 = M5TextBox(153, 108, "", lcd.FONT_UNICODE, 0x03cdff, rotate=0)

def btnRed0_wasPressed():
  label0.setText('Red')
  wait(1)
  label0.setText('')
  pass
dual_button_0.btnRed.wasPressed(btnRed0_wasPressed)

def btnBlue0_wasPressed():
  circle0 = M5Circle(160, 120, 30, 0xFFFFFF, 0xFFFFFF)
  wait(1)
  lcd.fill(0x000000)
  pass
dual_button_0.btnBlue.wasPressed(btnBlue0_wasPressed)