# ******************************************************************************************
# FileName     : 03._joystick_led_control.py
# Description  : 조이스틱 방향에 따라 LED 제어해 보기
# Author       : 박은정
# Created Date : 2023.08.28
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
Pin_VRx = ADC(Pin(A5))                   # 조이스틱 VRx(X축) 핀 지정
Pin_VRy = ADC(Pin(A4))                   # 조이스틱 VRy(Y축) 핀 지정

Pin_SW = Pin(D6)                         # 조이스틱 버튼 핀 지정

led_red = Pin(D2)                        # 빨강 LED 핀 지정
led_blue = Pin(D3)                       # 파랑 LED 핀 지정
led_green = Pin(D4)                      # 초록 LED 핀 지정
led_yellow = Pin(D5)                     # 노랑 LED 핀 지정

# 조이스틱 방향을 구하기 위한 변수 선언
# 조이스틱의 방향이 정확하지 않을 시 해당 변수의 값을 수정하세요.
joystick_mid_min_value = 1700            # 조이스틱 가운데 값 범위의 최소: 약 1700
joystick_mid_max_value = 2000            # 조이스틱 가운데 값 범위의 최대: 약 2000
min_value = joystick_mid_min_value - 500 # 조이스틱 북, 서 값의 범위: 0 ~ (1700 - 500)
max_value = joystick_mid_max_value + 500 # 조이스틱 남, 동 값의 범위: (2000 + 500) ~ 4095


# setup
def setup():
    Pin_VRx.atten(ADC.ATTN_11DB)         # 조이스틱 VRx 핀 입력 모드 설정
    Pin_VRy.atten(ADC.ATTN_11DB)         # 조이스틱 VRy 핀 입력 모드 설정

    Pin_SW.init(Pin.IN, Pin.PULL_UP)     # 조이스틱 버튼 입력 모드 설정

    led_red.init(Pin.OUT)                # 빨강 LED를 출력모드로 설정
    led_blue.init(Pin.OUT)               # 파랑 LED를 출력모드로 설정
    led_green.init(Pin.OUT)              # 초록 LED를 출력모드로 설정
    led_yellow.init(Pin.OUT)             # 노랑 LED를 출력모드로 설정

# loop
def loop():
    x_value = Pin_VRx.read()             # 조이스틱 x 좌표 값을 읽어옴
    y_value = Pin_VRy.read()             # 조이스틱 y 좌표 값을 읽어옴

    SW_value = Pin_SW.value()            # 조이스틱 버튼의 상태를 읽어옴

    # 빨강, 파랑, 초록 노랑 LED를 초기화
    led_red.value(LOW)
    led_blue.value(LOW)
    led_green.value(LOW)
    led_yellow.value(LOW)

    if SW_value == 0:                    # 조이스틱 버튼이 눌렸다면 모든 LED를 켬
        led_red.value(HIGH)
        led_blue.value(HIGH)
        led_green.value(HIGH)
        led_yellow.value(HIGH)

    if y_value < min_value:              # y_value가 min_value 미만이라면 빨강 LED를 켬
        led_red.value(HIGH)
    elif y_value < max_value:            # y_value가 max_value 미만이라면 pass
        pass
    elif y_value >= max_value:           # y_value가 max_value 이상이라면 노랑 LED를 켬
        led_yellow.value(HIGH)

    if x_value < min_value:              # x_value가 min_value 미만이라면 파랑 LED를 켬
        led_blue.value(HIGH)
    elif x_value < max_value:            # x_value가 max_value 미만이라면 pass
        pass
    elif x_value >= max_value:           # x_value가 max_value 이상이라면 초록 LED를 켬
        led_green.value(HIGH)

    time.sleep(0.1)                      # 0.1초 대기


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