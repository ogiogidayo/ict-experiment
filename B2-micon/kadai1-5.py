from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x000000)
light_0 = unit.get(unit.LIGHT, unit.PORTB)
label0 = M5TextBox(153, 102, "明るさは", lcd.FONT_UNICODE, 0x03cdff, rotate=0)
wait(1)
label0.setText(str(light_0.analogValue))