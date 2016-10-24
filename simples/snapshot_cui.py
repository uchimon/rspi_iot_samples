#!/usr/bin/python
# coding:utf-8

#open CV2を利用してUSBカメラから画像を取得する
#cuiのみ、ウィンドウ無しでの利用の場合。
#

import cv2
from time import gmtime, strftime

def capture_camera(mirror=True, size=None):
    ############################
    #ファイル名
    fname = 'tmp/' + strftime('%Y%m%d_%H%M%S.png', gmtime())

    #usbデバイス番号
    #基本的には0で良さそう。カメラによってはラズパイの再起動が必要
    dev = 0
    ###########################

    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(dev) # 0はカメラのデバイス番号

    # retは画像を取得成功フラグ
    ret, frame = cap.read()

    # 鏡のように映るか否か
    if mirror is True:
        frame = frame[:,::-1]

    # フレームをリサイズ
    # sizeは例えば(800, 600)
    if size is not None and len(size) == 2:
        frame = cv2.resize(frame, size)

    cv2.imwrite(fname, frame)

    # キャプチャを解放する
    cap.release()
    return fname

####メイン処理
print(capture_camera())

