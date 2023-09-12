# ******************************************************************************************
# FileName     : 03._neopixel_led_rgb.py
# Description  : 1초마다 빨강, 파랑, 초록 색상으로 네오픽셀 LED 켜 보기
# Author       : 박은정
# Created Date : 2023.9.12
# Reference    :
# Modified     : 
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
import neopixel


# variable
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12) # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화


#setup
def setup():                                 # pass를 사용하여 건너뜀
    pass


#loop
def loop():
    np[0] = (255, 0, 0)                      # 네오픽셀의 색상을 빨강으로 지정
    np.write()                               # 네오픽셀 출력
    time.sleep(1)                            # 1초간 대기

    np[0] = (0, 255, 0)                      # 네오픽셀의 색상을 초록으로 지정
    np.write()                               # 네오픽셀 출력
    time.sleep(1)                            # 1초간 대기

    np[0] = (0, 0, 255)                      # 네오픽셀의 색상을 파랑 으로 지정
    np.write()                               # 네오픽셀 출력
    time.sleep(1)                            # 1초간 대기


if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================