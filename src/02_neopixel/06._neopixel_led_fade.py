# ******************************************************************************************
# FileName     : 06._neopixel_led_fade.py
# Description  : 네오픽셀 첫 번째 LED 밝기 조절해 보기
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
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12)   # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화


#setup
def setup():                                   # pass를 사용하여 건너뜀
    pass


#loop
def loop():
    for i in range(0, 256):
        np[0] = (i, 0, 0)                      # 네오픽셀[0]의 색상을 점점 밝아지게 설정
        np.write()                             # 네오픽셀 출력
        time.sleep(0.01)                       # 1초간 대기


if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================