from m5stack import *
from m5ui import *
from uiflow import *
import time
remoteInit()

setScreenColor(0x222222)
label0 = M5TextBox(139, 112, "label0", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def _remote_ButtonName():
  label0.setText('Hello M5')
  wait(1)
  label0.setText('')