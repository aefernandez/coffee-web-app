# import libraries
import RPi.GPIO as GPIO
from flask import Flask, render_template
import datetime

# Configure GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define GPIOs
#pump_pin = 13

#define output pins
#GPIO.setup(pump_pin, GPIO.out)

#Intialize pins
#GPIO.output(pump_pin, GPIO.low)


app = Flask(__name__)
@app.route("/")
def index():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):

   # do some pre-processing of the command
   # ensure that we don't act unexpectedly on 
   # random commands

   # translate device name to pin 
   if deviceName == 'pump':
      actuator = pump_pin

   # toggle the pin
   if action == "on":
      GPIO.output(actuator, GPIO.HIGH)
   elif action == "off":
      GPIO.output(actuator, GPIO.LOW)
   else
      # print an error statement and do nothing

   # change the status on the UI

   return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)