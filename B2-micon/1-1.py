from m5stack import *
from m5ui import *
from uiflow import *


setScreenColor(0x186771)






Sample = M5TextBox(110, 100, "Sample txt", lcd.FONT_UNICODE, 0x03cdff, rotate=0)
circle0 = M5Circle(66, 225, 15, 0xFFFFFF, 0xFFFFFF)
circle1 = M5Circle(160, 225, 15, 0xFFFFFF, 0xFFFFFF)
circle2 = M5Circle(256, 225, 15, 0xFFFFFF, 0xFFFFFF)