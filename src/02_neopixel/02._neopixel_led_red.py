 ******************************************************************************************
# FileName     : 02._neopixel_led_red.py
# Description  : 네오픽셀 LED를 빨간색으로 켜 보기
# Author       : 박은정
# Created Date : 2023.9.12
# Reference    :
# Modified     : 
# ******************************************************************************************


# import
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


if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================