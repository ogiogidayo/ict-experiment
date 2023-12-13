from m5stack import *
from m5ui import *
from uiflow import *
import unit


setScreenColor(0x000000)
accel_0 = unit.get(unit.ACCEL, unit.PORTA)

label1 = M5TextBox(53, 148, "X", lcd.FONT_Default, 0xff0000, rotate=0)
label2 = M5TextBox(132, 148, "Y", lcd.FONT_Default, 0x6eff00, rotate=0)
label3 = M5TextBox(226, 148, "Z", lcd.FONT_Default, 0x1900ff, rotate=0)


while True:
  label1.setText(str(accel_0.acceleration[0]))
  label2.setText(str(accel_0.acceleration[1]))
  label3.setText(str(accel_0.acceleration[2]))
  wait_ms(2)
  
#   重力加速度