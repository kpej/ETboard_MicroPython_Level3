# ******************************************************************************************
# FileName     : 02._joystick_status_print.py
# Description  : 조이스틱 상태를 쉘에 출력해 보기
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
Pin_VRx = ADC(Pin(A5))                   # 조이스틱 VRx(X축) 핀 지정
Pin_VRy = ADC(Pin(A4))                   # 조이스틱 VRy(Y축) 핀 지정

Pin_SW = Pin(D6)                         # 조이스틱 버튼 핀 지정

# 조이스틱 방향을 구하기 위한 변수 선언
# 조이스틱의 방향이 정확하지 않을 시 해당 변수의 값을 수정하세요.
joystick_mid_min_value = 1700            # 조이스틱 중간 최소 값: 약 1700
joystick_mid_max_value = 2000            # 조이스틱 중간 최대 값: 약 2000
min_value = joystick_mid_min_value - 500 # 조이스틱 북, 서 값의 범위: 0 ~ 1700 - 500
max_value = joystick_mid_max_value + 500 # 조이스틱 남, 동 값의 범위: 2000 + 500 ~ 4095


#setup
def setup():
    Pin_VRx.atten(ADC.ATTN_11DB)         # 조이스틱 VRx(X축) 핀 입력 모드 설정
    Pin_VRy.atten(ADC.ATTN_11DB)         # 조이스틱 VRy(Y축) 핀 입력 모드 설정
    
    Pin_SW.init(Pin.IN, Pin.PULL_UP)     # 조이스틱 버튼 입력 모드 설정


#loop
def loop():
    x_value = Pin_VRx.read()             # x 좌표값을 읽어옴
    y_value = Pin_VRy.read()             # y 좌표값을 읽어옴

    SW_value = Pin_SW.value()            # 버튼의 상태를 읽어옴

    print('조이스틱 방향: ', end = '')

    if y_value < min_value:              # y_value가 min_value 미만이라면 '북' 출력
        print('북', end = '')
    elif y_value >= max_value:           # y_value가 max_value 이상이라면 '남' 출력
        print('남', end = '')

    if x_value < min_value:              # x_value가 min_value 미만이라면 '서' 출력
        print('서', end = '')
    elif x_value >= max_value:           # x_value가 max_value 이상이라면 '동' 출력
        print('동', end = '')

    # x_value와 y_value의 값이 중간 값 범위에 속한다면 '중간' 출력
    if(x_value >= min_value and x_value < max_value and y_value >= min_value and y_value < max_value):
        print('중간', end = '')

    print('')                            # 줄바꿈

    print('버튼의 상태: ', end = '')

    if SW_value == 1:                    # 버튼의 상태가 1이라면 '버튼이 눌리지 않음'을 출력
        print('버튼이 눌리지 않음')
    else:                                # 버튼의 상태가 0이라면 '버튼이 눌림'을 출력
        print('버튼이 눌림')

    time.sleep(0.1)                      # 0.1초 대기 

if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================