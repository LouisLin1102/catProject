
from lib2to3.pgen2.pgen import DFAState
from os import urandom
import time
from cloud.function import LintBotFunction
from mqtt.mq_main import SendMessageFunction
import mqtt.mq as mq
import datetime
import argparse
import json
import cloud.bigQuery as bq
import RPi.GPIO as GPIO
import picamera 


parser = argparse.ArgumentParser()
parser.add_argument('--project_id', type=str, default='catproject-338203',
                        help='project_id')
parser.add_argument('--cloud_region', type=str, default='asia-east1',
                        help='cloud_region')
parser.add_argument('--registry_id', type=str, default='Pi_IoT',
                        help='registry_id')
parser.add_argument('--device_id', type=str, default='raspe-device',
                        help='device_id')
parser.add_argument('--private_key_file', type=str, default='main/rsa_private.pem',
                        help='private_key_file')
parser.add_argument('--algorithm', type=str, default='RS256',
                        help='algorithm')
parser.add_argument('--ca_certs', type=str, default='main/roots.pem',
                        help='ca_certs')
parser.add_argument('--mqtt_bridge_hostname', type=str, default='mqtt.googleapis.com',
                        help='mqtt_bridge_hostname')
parser.add_argument('--mqtt_bridge_port', type=int, default=8883,
                        help='mqtt_bridge_port')
parser.add_argument('--num_messages', type=int, default=1,
                        help='num_messages')
parser.add_argument('--message_type', type=str, default='event',
                        help='message_type')
parser.add_argument('--jwt_expires_minutes', type=int, default=1,
                        help='jwt_expires_minutes')
args = parser.parse_args()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(29,GPIO.IN)
GPIO.setup(31,GPIO.OUT)

trigger_pin = 16
echo_pin = 18

GPIO.setup(trigger_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)

oosCount = 3
svaePhotoPath = "/home/pi/Public/"

def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1
        
def get_distance():
    time.sleep(2)
    send_trigger_pulse()
    wait_for_echo(True, 5000)
    start = time.time()
    wait_for_echo(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340 *100 /2
    print("distance_cm", distance_cm)
    return (distance_cm)

def takePhoto():
    camera = picamera.PiCamera()
    time.sleep(2)
    sourceFile = svaePhotoPath + "image.jpg"
    camera.capture(sourceFile)
    #bq.UploadPhoto(sourceFile)

while True:
    try:
        #takePhoto()
        time.sleep(1)
        flag = GPIO.input(29)
        if flag == 0:
            print("No intruders",flag,", ", datetime.datetime.now())
            GPIO.output(31,0)
            time.sleep(1)
        elif flag == 1:
            print("INtruder detected",flag,", ", datetime.datetime.now())
            time.sleep(3)
            inTime = datetime.datetime.now() 
            while get_distance() > 1:
                GPIO.output(31,1)
                time.sleep(1)
            
            GPIO.output(31,0)
            time.sleep(1)
            outTime = datetime.datetime.now() 
            date = datetime.datetime.strftime( datetime.date.today(),'%Y-%m-%d')
            print("inTime" , inTime)
            print("outTime" , outTime)
            print("date" , date)
            if (outTime - inTime ).seconds > 3 :
                druation = str(((outTime - inTime).seconds))
                print(druation)
                sendMessage = SendMessageFunction(args,date,inTime,outTime,druation)
                #sendMessage.push_message()
                time.sleep(2)
                number = bq.QueryDataCount(date)
                #print(number)
                if int(number) > oosCount:
                    push_str = ("累積上廁所次數 {} 快點鏟貓屎啊!!").format(number)
                    print(push_str)
                    #lineBot = LintBotFunction(push_str)
                    #lineBot.push_message()
                    takePhoto()

            time.sleep(3)
    except Exception as error:
            print(error)
            GPIO.cleanup()
