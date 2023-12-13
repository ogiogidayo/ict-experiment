from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import json



setScreenColor(0x222222)


data = None
label0 = M5TextBox(139, 112, "label0", lcd.FONT_Default, 0xFFFFFF, rotate=0)

def buttonA_wasPressed():
  global data
  label0.setText('accsess...')
  try:
    req = urequests.request(method='GET', url='http://api.openweathermap.org/data/2.5/weather?q=gunma&appid=bb2d92d48fdded5f905b4551b371c69c')
    data = json.loads((req.text))
    label0.setText(str((data['weather'])[-1]['main']))
    gc.collect()
    req.close()
  except:
    label0.setText(str((str('fail:') + str(str((req.status_code))))))
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global data
  label0.setText('accsess...')
  try:
    req = urequests.request(method='GET', url='http://api.openweathermap.org/data/2.5/weather?q=gunma&appid=bb2d92d48fdded5f905b4551b371c69c')
    data = json.loads((req.text))
    label0.setText(str((data['main'])['temp']-273))
    gc.collect()
    req.close()
  except:
    label0.setText(str((str('fail:') + str(str((req.status_code))))))
  pass
btnB.wasPressed(buttonB_wasPressed)