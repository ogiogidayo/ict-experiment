from m5stack import *
from m5ui import *
from uiflow import *
from easyIO import *

setScreenColor(0x222222)
label0 = M5TextBox(140, 120, "X", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(180, 120, "Y", lcd.FONT_Default,0xFFFFFF, rotate=0)

while True:
  label0.setText(str(analogRead(34)))
  label1.setText(str(analogRead(35)))
  wait(0.1)