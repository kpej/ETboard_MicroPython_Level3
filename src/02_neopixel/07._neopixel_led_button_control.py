# ******************************************************************************************
# FileName     : 07._neopixel_led_button_control.py
# Description  : 빨강 버튼을 눌러 네오픽셀에서 빨강 LED를 켜 보기
# Author       : 박은정
# Created Date : 2023.9.12
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정 
# ******************************************************************************************


# import
from machine import ADC, Pin
from ETboard.lib.pin_define import *
import neopixel


# global variable
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12)   # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화

button_red = Pin(D6)                           # 빨강 버튼의 핀 지정


# setup
def setup():                                   # pass를 사용하여 건너뜀
    pass


# loop
def loop():
    button_red_status = button_red.value()     # 빨강 버튼의 값을 저장

    np[0] = (0, 0, 0)                          # 네오픽셀[0]의 색상을 초기화

    if button_red_status == LOW:               # 빨강 버튼이 눌렸다면
        np[0] = (255, 0, 0)                    # 네오픽셀[0]의 색상을 빨강으로 설정
        np.write()                             # 네오픽셀 출력

    np.write()                                 # 네오픽셀 출력


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