from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x186771)

label0 = M5TextBox(150, 100, "a", lcd.FONT_UNICODE, 0x03cdff, rotate=0)


def buttonA_wasPressed():
  label0.setText('A')
  wait(1)
  label0.setText('a')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  circle0 = M5Circle(160, 120, 30, 0xFFFFFF, 0xFFFFFF)
  wait(1)
  lcd.fill(0x186771)
  pass
btnB.wasPressed(buttonB_wasPressed)