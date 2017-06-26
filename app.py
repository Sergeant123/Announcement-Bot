#Note, this bot was created to respond to a friend in chat who repeats same pictures and phrases

import os
import sys
import json
import random          
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

satania = ['https://i.groupme.com/1280x720.png.4876a31d98d043f19873136abd816e40'
          ]
           


app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  sentence = data['text']

#############################################
  negatives = ["not", "nobody", "cannot", "knot"]
          
  if data['name'] != 'Lunar Bot':
    for i in range(len(negatives)):    
      if negative[i] in sentence.lower():
        msg = "this word is included in list"
        send_message(msg)
      elif "no" in sentence.lower():
        msg = "no u"
        send_message(msg)
    if "911" in data['text']:
           msg = '911'
           send_message(msg)
  if data['text'] == '!lasagna':
    num = random.randint(0,len(satania)-1)
    msg = satania[num]
    send_message(msg)


#########################################
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
sys.stdout.flush()
