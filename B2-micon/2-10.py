from m5stack import *
from m5ui import *
from uiflow import *
import urequests


setScreenColor(0x222222)


message = None



label0 = M5TextBox(139, 106, "label0", lcd.FONT_Default, 0xFFFFFF, rotate=0)


# この関数の説明…
def post(message):
  label0.setText('access...')
  try:
    req = urequests.request(method='POST', url='https://maker.ifttt.com/trigger/hoge/with/key/[API_Key]}',json={'value1':message})
    label0.setText('Sucsess')
    gc.collect()
    req.close()
  except:
    label0.setText('Failed')


def buttonA_wasPressed():
  global message
  post('A was Pressed!')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global message
  post('B was Pressed!')
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global message
  post('C was Pressed!')
  pass
btnC.wasPressed(buttonC_wasPressed)