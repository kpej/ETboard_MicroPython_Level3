# ******************************************************************************************
# FileName     : neopixel_sensor_light.py
# Description  : 사람이 감지되면 네오픽셀 켜 보기
# Author       : 박은정
# Created Date : 2023.11.22
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정 
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *
import neopixel


# global variable
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12) # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화
PinPiR = Pin(D3)


# setup
def setup():                                 # pass를 사용하여 건너뜀
    pass


# loop
def loop():
    for i in range(0, 12):
        np[i] = (0, 0, 0)
    np.write()
        
    if PinPiR.value() == HIGH:               # 인체 감지 센서의 값이 HIGH라면 네오픽셀 출력
        for i in range(0, 12):
            np[i] = (255, 0, 0)
        np.write()


if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
