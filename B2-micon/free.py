from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import json
import unit

# default setting
setScreenColor(0xe1a206)
data = None
pir_0 = unit.get(unit.PIR, unit.PORTA)
label0 = M5TextBox(26, 165, "News", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
label1 = M5TextBox(128, 32, "Hello!", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
label2 = M5TextBox(26, 83, "Whether", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
label3 = M5TextBox(116, 125, "Detail", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
label4 = M5TextBox(26, 205, "Title", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label5 = M5TextBox(26, 125, "Gunma:", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
label6 = M5TextBox(196, 125, "", lcd.FONT_Comic, 0xFFFFFF, rotate=0)
line1 = M5Line(M5Line.PLINE, 25, 155, 300, 155, 0xFFFFFF)

# ログをスプシに送信する関数
def post_log():
  global data
  label0.setText('access...')
  try:
    req = urequests.request(method='POST', url='https://maker.ifttt.com/trigger/hoge/with/key/XAuoUVZUPth7sTFXseqYX',json={'value1':'Accsessed'})
    label0.setText('Sucsess')
    gc.collect()
    req.close()
  except:
    label0.setText('Failed')

# newsapiを叩く関数
def get_news():
  global data
  label4.setText('access...')
  try:
    headers = {
      'X-Api-Key': '[API_Key]',
      'User-Agent': 'Macbook'
    }
    url ='https://newsapi.org/v2/everything?q=EC2&sortBy=publishedAt&pageSize=1'
    req = urequests.request(method='GET', url=url, headers=headers)
    data = json.loads((req.text))
    title = data['articles'][-1]['title']
    label4.setText(str(title))
    gc.collect()
    req.close()
  except:
    label4.setText('Failed')
    
# openweathermapを叩く関数
def get_weather():
  global data
  label3.setText('accsess...')
  try:
    req = urequests.request(method='GET', url='http://api.openweathermap.org/data/2.5/weather?q=gunma&appid=[API_Key]')
    data = json.loads((req.text))
    label3.setText(str((data['weather'])[-1]['main']))
    label6.setText(str(int((data['main'])['temp']-273))+"\u00B0C")
    gc.collect()
    req.close()
  except:
    label3.setText(str((str('fail:') + str(str((req.status_code))))))
  pass

count = 0
while str(pir_0.state) == '1':
  if count > 99: # 100回以上APIを叩くのを防ぐ 
    break
  post_log()
  get_weather()
  get_news()
  wait(360)
  count += 1