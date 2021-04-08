#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!usr/bin/env python
# -*- coding: utf-8 -*-


import RPi.GPIO
import time
from flask import Flask


RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2, RPi.GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/start')
def start():
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(2,RPi.GPIO.OUT)
        while(True):
            RPi.GPIO.output(2,False)
            time.sleep(5)
            RPi.GPIO.output( 2,True)
            time.sleep(5)

RPi.GPIO.cleanup()

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)

