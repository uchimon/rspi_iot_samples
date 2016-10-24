#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#DHT11, DHT22を用いて温度と湿度を取得
#前提条件：
# Adafruitのpythonをインストール済み(https://github.com/adafruit/Adafruit_Python_DHT) 
#

import sys
from time import gmtime, strftime

import Adafruit_DHT

######利用するセンサー
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22

#####GPIOピン番号
args = sys.argv
pin = args[1]


def get_DHT():
    humid = 0
    temp = 0

    try:
        humid, temp = Adafruit_DHT.read_retry(sensor, pin)
    except:
        pass
    return humid, temp

##[メイン処理]#######################
h, t = get_DHT()

#output3
#時刻を追加
print("{0},{1},{2},".format(strftime('%Y-%m-%d %H:%M:%S', gmtime()), t, h))
