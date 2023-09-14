# ******************************************************************************************
# FileName     : 01_water_pump_sample1.py
# Description  : 버튼으로 워터펌프 제어하기
# Author       : 손철수
# Created Date : 2023.09.14
# Reference    :
# Modified     : 
# ******************************************************************************************

# import
import time
from machine import Pin
from ETboard.lib.pin_define import *

# global variable
led_red = Pin(D2)                              # 빨강 LED 핀 지정
led_blue = Pin(D3)                             # 파랑 LED 핀 지정
button_red = Pin(D6)                           # 빨강 버튼 핀 지정
button_blue = Pin(D7)                          # 버튼 핀 지정

# setup
def setup() :
    led_red.init(Pin.OUT)                      # 빨강 LED 출력모드 설정
    led_blue.init(Pin.OUT)                     # 파랑 LED 출력모드 설정
    button_red.init(Pin.IN)                    # 빨강 버튼 입력모드 설정하기
    button_blue.init(Pin.IN)                   # 버튼 입력모드 설정하기
    stop_left_pump()
    
# main loop
def loop() :
    
    # 빨강 버튼 상태 저장하기
    button_red_value = button_red.value()
    button_blue_value = button_blue.value()
    
    # 빨강 버튼으로 
    if button_red_value == 0:
        run_left_pump()
        time.sleep(0.3)
    if button_blue_value == 0:
        stop_left_pump()
        time.sleep(0.3)
    
    
def run_left_pump():
    led_red.value(HIGH)                        # 빨강 LED 켜기
    led_blue.value(LOW)                        # 파랑 LED 끄기
    
def stop_left_pump():
    led_red.value(LOW)                         # 빨강 LED 끄기
    led_blue.value(LOW)                        # 파랑 LED 끄기    


if __name__ == "__main__" :
    setup()
    while True :
        loop()
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================