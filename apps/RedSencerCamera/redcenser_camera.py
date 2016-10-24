#!/usr/bin/python
# coding:utf-8

import sys
sys.path.append('./libs')

import RPi.GPIO as GPIO
from time import sleep
#from libs import snapshot as snap
import snapshot as snap
#from libs import aws_iot_pub as iot
import aws_iot_pub as iot
import commands
#import system
#from subprocess import check_call

import ConfigParser

#設定ファイルの読み込み
inifile = ConfigParser.SafeConfigParser()
inifile.read('conf/config.ini')

bucket = inifile.get('main', 's3bucket')
domain = inifile.get('main', 's3domain')

def cencer_callback(ch):
    print('hi')
    print(ch)
    path = snap.capture_camera()
    print(path)

    #s3にアップロードするコマンド
    #os.system('aws s3 cp ' + path + ' s3://' + bucket  +  ' --acl public-read')
    cmd = 'aws s3 cp ' + path + ' s3://' + bucket  +  ' --acl public-read'
    print(cmd)
    #check_call([cmd])
    commands.getoutput(cmd)
    arr = path.split('/')
    size = len(arr)
    url = 'https://' + domain + '/' + bucket +  '/' + arr[size -1]
    print(url)
    iot.publish(url)

pin = 10

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

GPIO.add_event_detect(pin, GPIO.RISING, callback=cencer_callback, bouncetime=1000)

try:
    while True:
#        if GPIO.input(pin) == GPIO.HIGH:
#            print("1:not obstacled")
#        else:
#            print("0:obstacled")
        sleep(0.5)
except:
    pass

GPIO.cleanup(pin)

