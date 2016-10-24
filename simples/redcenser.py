#!/usr/bin/python
# coding:utf-8

#赤外線遮断レーザーを利用
#起動するとコンソールに処理結果を表示。
#Ctl + Cで終了
#

import RPi.GPIO as GPIO
from time import sleep

#pin番号
pin = 10

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

try:
    while True:
        if GPIO.input(pin) == GPIO.HIGH:
            print("1:not blocked")
        else:
            print("0:blocked")
        sleep(0.5)
except:
    pass

GPIO.cleanup(pin)
print("proc is end.")

