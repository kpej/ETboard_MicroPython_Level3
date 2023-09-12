# ******************************************************************************************
# FileName     : 08._neopixel_led_button_control_2.py
# Description  : 버튼을 눌러 네오픽셀에서 같은 색상의 LED를 켜 보기
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
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12)     # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화

button_red = Pin(D6)                             # 빨강 버튼 핀 지정
button_blue = Pin(D7)                            # 파랑 버튼 핀 지정
button_green = Pin(D8)                           # 초록 버튼 핀 지정
button_yellow = Pin(D9)                          # 노랑 버튼 핀 지정


#setup
def setup():                                     # pass를 사용하여 건너뜀
    pass


#loop
def loop():
    button_red_status = button_red.value()       # 빨강 버튼의 값을 저장
    button_blue_status = button_blue.value()     # 파랑 버튼의 값을 저장
    button_green_status = button_green.value()   # 초록 버튼의 값을 저장
    button_yellow_status = button_yellow.value() # 노랑 버튼의 값을 저장

    np[0] = (0, 0, 0)                            # 네오픽셀[0]의 색상을 초기화

    if button_red_status == LOW:                 # 빨강 버튼이 눌렸다면
        np[0] = (255, 0, 0)                      # 네오픽셀[0]의 색상을 빨강으로 설정
        np.write()                               # 네오픽셀 출력

    if button_blue_status == LOW:                # 파랑 버튼이 눌렸다면
        np[0] = (0, 0, 255)                      # 네오픽셀[0]의 색상을 파랑으로 설정
        np.write()                               # 네오픽셀 출력
  
    if button_green_status == LOW:               # 초록 버튼이 눌렸다면
        np[0] = (0, 255, 0)                      # 네오픽셀[0]의 색상을 초록으로 설정
        np.write()                               # 네오픽셀 출력

    if button_yellow_status == LOW:              # 노랑 버튼이 눌렸다면
        np[0] = (255, 255, 0)                    # 네오픽셀[0]의 색상을 노랑으로 설정
        np.write()                               # 네오픽셀 출력

    np.write()                                   # 네오픽셀 출력


if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================