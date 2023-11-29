# ******************************************************************************************
# FileName     : joystick_status_oled_print
# Description  : 조이스틱 상태를 OLED에 출력해 보기
# Author       : 박은정
# Created Date : 2023.08.28
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
from ETboard.lib.OLED_U8G2 import *


# global variable
Pin_VRx = ADC(Pin(A5))                   # 조이스틱 VRx(X축) 핀 지정
Pin_VRy = ADC(Pin(A4))                   # 조이스틱 VRy(Y축) 핀 지정

Pin_SW = Pin(D6)                         # 조이스틱 버튼 핀 지정

oled = oled_u8g2()                       # OLED 선언

# 조이스틱 방향을 구하기 위한 변수 선언
# 조이스틱의 방향이 정확하지 않을 시 해당 변수의 값을 수정하세요.
joystick_mid_min_value = 1700            # 조이스틱 중간 최소 값: 약 1700
joystick_mid_max_value = 2000            # 조이스틱 중간 최대 값: 약 2000
min_value = joystick_mid_min_value - 500 # 조이스틱 북, 서 값의 범위: 0 ~ 1700 - 500
max_value = joystick_mid_max_value + 500 # 조이스틱 남, 동 값의 범위: 2000 + 500 ~ 4095


# setup
def setup():
    Pin_VRx.atten(ADC.ATTN_11DB)         # 조이스틱 VRx(X축) 핀 입력 모드 설정
    Pin_VRy.atten(ADC.ATTN_11DB)         # 조이스틱 VRy(Y축) 핀 입력 모드 설정

    Pin_SW.init(Pin.IN, Pin.PULL_UP)     # 조이스틱 버튼 입력 모드 설정


# loop
def loop():
    x_value = Pin_VRx.read()             # x 좌표값을 읽어옴
    y_value = Pin_VRy.read()             # y 좌표값을 읽어옴

    SW_value = Pin_SW.value()            # 버튼의 상태를 읽어옴

    direction = ''

    oled.clear()                         # OLED 초기화
    oled.setLine(1, "et.ketri.re.kr")

    if y_value < min_value:              # y_value가 min_value 미만이라면 direction에 'north' 저장
        direction = 'north'
    elif y_value >= max_value:           # y_value가 max_value 이상이라면 direction에 'south' 저장
        direction = 'south'

    if x_value < min_value:              # x_value가 min_value 미만이라면 direction에 'west' 저장
        direction = direction + 'west'
    elif x_value >= max_value:           # x_value가 max_value 이상이라면 direction에 'east' 저장
        direction = direction + 'east'

    # x_value와 y_value의 값이 중간 값 범위에 속한다면 변수 direction에 'mid' 저장
    if(x_value >= min_value and x_value < max_value and y_value >= min_value and y_value < max_value):
        direction = 'mid'

    oled.setLine(2, direction)           # direction 변수에 저장된 방향을 OLED 2번째 줄에 저장

    if SW_value == 1:                    # 버튼의 상태가 1이라면 OLED 3번째 줄에 'not pressed'를 저장
        oled.setLine(3, 'not pressed')
    else:                                # 버튼의 상태가 0이라면 OLED 3번째 줄에 'pressed'를 저장
        oled.setLine(3, 'pressed')

    oled.display()                       # OLED에 저장된 문자열을 출력

    time.sleep(0.1)                      # 0.1초 대기


# start point
if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================