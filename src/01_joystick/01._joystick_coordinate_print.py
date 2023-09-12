# ******************************************************************************************
# FileName     : 01._joystick_coordinate_print.py
# Description  : 조이스틱 좌표 값을 쉘에 출력해 보기
# Author       : 박은정
# Created Date : 2023.08.28
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# variable
Pin_VRx = ADC(Pin(A5))                # 조이스틱 VRx(X축) 핀 지정
Pin_VRy = ADC(Pin(A4))                # 조이스틱 VRy(y축) 핀 지정


#setup
def setup():
    Pin_VRx.atten(ADC.ATTN_11DB)      # VRx 핀 모드를 입력 모드로 설정
    Pin_VRy.atten(ADC.ATTN_11DB)      # VRy 핀 모드를 입력 모드로 설정


#loop
def loop():
    x_value = Pin_VRx.read()          # 조이스틱 VRx 값을 읽어옴
    y_value = Pin_VRy.read()          # 조이스틱 VRy 값을 읽어옴

    # X축과 Y축의 값을 출력
    print("X 좌표: " + str(x_value) +", Y 좌표: " + str(y_value))

    time.sleep(0.1)                   # 0.1초 대기 


if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================