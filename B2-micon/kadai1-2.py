from m5stack import *
from m5ui import *
from uiflow import *


setScreenColor(0x186771)






Sample = M5TextBox(110, 100, "Sample txt", lcd.FONT_UNICODE, 0x03cdff, rotate=0)
circle0 = M5Circle(66, 225, 15, 0xFFFFFF, 0xFFFFFF)
circle1 = M5Circle(160, 225, 15, 0xFFFFFF, 0xFFFFFF)
circle2 = M5Circle(256, 225, 15, 0xFFFFFF, 0xFFFFFF)
a = M5TextBox(51, 180, "Push!!", lcd.FONT_Default, 0xFFFFFF, rotate=0)
b = M5TextBox(138, 180, "Push!!", lcd.FONT_Default, 0xFFFFFF, rotate=0)
c = M5TextBox(234, 180, "Push!!", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def buttonA_wasPressed():
  # global params
  a.setText('Pushed!!')
  Sample.setText('A button!')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  b.setText('Pushed!!')
  Sample.setText('B button')
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  # global params
  c.setText('Pushed!!')
  Sample.setText('C buttun')
  pass
btnC.wasPressed(buttonC_wasPressed)


Sample.setText('Hello M5')