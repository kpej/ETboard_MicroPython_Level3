#*******************************************************************************************
# FileName     : 01._neopixel_led_control.py
# Description  : 네오픽셀 LED를 1초 간격으로 켰다 껐다 해 보기
# Author       : 박은정
# Created Date : 2023.9.12
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정 
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
import neopixel


# global variable
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12) # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화


# setup
def setup():                                 # pass를 사용하여 건너뜀
    pass


# loop
def loop():
    np[0] = (255, 0, 0)                      # 네오픽셀의 색상을 빨강으로 지정
    np.write()                               # 네오픽셀 출력
    time.sleep(1)                            # 1초간 대기

    np[0] = (0, 0, 0)                        # 네오픽셀의 초기화
    np.write()                               # 네오픽셀 출력
    time.sleep(1)                            # 1초간 대기


# start point
if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================