from m5stack import *
from m5ui import *
from uiflow import *
import unit
setScreenColor(0x222222)
servo0 = unit.get(unit.SERVO, unit.PORTC)

while True:
  servo0.write_angle(30)
  wait(1)
  servo0.write_angle(60)
  wait(1)