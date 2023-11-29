# ******************************************************************************************
# FileName     : buzzer_timer.py
# Description  : 빨강 버튼을 눌러 네오픽셀에서 빨강 LED를 켜 보기
# Author       : 박은정
# Created Date : 2023.9.19
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정, 함수 수정
# ******************************************************************************************


# import
import machine
import time
from machine import Pin
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *


# global variable
oled = oled_u8g2()                            # OLED 선언

buzzer = Pin(D6)                              # 부저 핀 지정

button_blue = Pin(D7)                         # 파랑 버튼 핀 지정
button_green = Pin(D8)                        # 초록 버튼 핀 지정
button_yellow = Pin(D9)                       # 노랑 버튼 핀 지정

button_blue_value = 0                         # 파랑 버튼의 상태
button_blue_old_value = 1                     # 파랑 버튼의 이전 상태

button_green_value = 0                        # 초록 버튼의 상태
button_green_old_value = 1                    # 초록 버튼의 이전 상태

button_yellow_value = 0                       # 노랑 버튼의 상태
button_yellow_old_value = 1                   # 노랑 버튼의 이전 상태

timer = 0
sec = 0
minute = 0


# setup
def setup():
    buzzer.init(Pin.OUT)

    button_blue.init(Pin.IN)                  # 파랑 버튼 입력모드 설정하기
    button_green.init(Pin.IN)                 # 초록 버튼 입력모드 설정하기
    button_yellow.init(Pin.IN)                # 노랑 버튼 입력모드 설정하기


# calc_time
def calc_time():
    # 전역변수 호출
    global timer, minute, sec
    
    minute = timer // 60                      # timer를 60으로 나눈 몫
    sec = timer % 60                          # timer를 60으로 나눈 나머지  


# start_timer
def start_timer():
    # 전역변수 호출
    global timer, minute, sec

    oled.clear()                              # OLED 초기화
    oled.setLine(1, "timer start!")           # OLED 첫 번째 줄에 "timer start!" 출력

    calc_time()                               # calc_time 함수 호출
    # minute, sec 변수를 00:00 형식으로 문자열 생성
    timer_str = "{:02d}:{:02d}".format(minute, sec)
    oled.setLine(2, timer_str)                # OLED 두 번째 줄에 timer_str 출력

    oled.display()

    for i in range(0, timer):
        timer = timer - 1                     # 타이머를 1초씩 감소

        oled.clear()

        oled.setLine(1, "timer start!")       # OLED 첫 번째 줄에 "timer start!" 출력

        calc_time()                           # calc_time 함수 호출
        # minute, sec 변수를 00:00 형식으로 문자열 생성
        timer_str = "{:02d}:{:02d}".format(minute, sec)
        oled.setLine(2, timer_str)            # OLED 두 번째 줄에 timer_str 출력

        oled.display()

        time.sleep(1)

    for i in range(5):                        # 부저에서 소리를 재생
        for j in range(80):
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)
        time.sleep(1)


# loop
def loop():
    # 전역변수 호출
    global timer, sec, minute,\
    button_blue_value, button_blue_old_value,\
    button_green_value, button_green_old_value,\
    button_yellow_value, button_yellow_old_value

    # 파랑, 초록, 노랑 버튼의 상태 저장
    button_blue_value = button_blue.value()
    button_green_value = button_green.value()
    button_yellow_value = button_yellow.value()

    oled.clear()                              # OLED 초기화

    oled.setLine(1, "set timer!")             # OLED 첫 줄에 "set timer!" 출력

    # 파랑 버튼을 눌렀다 뗀 상태라면
    if button_blue_value == 0 and button_blue_old_value == 1:
        timer = timer + 60                    # timer 변수에 60을 더함
    button_blue_old_value = button_blue_value

    # 초록 버튼을 눌렀다 뗀 상태라면
    if button_green_value == 0 and button_green_old_value == 1:
        timer = timer - 60                    # timer 변수에 60을 뺌
        if timer < 0:                         # timer가 0보다 작다면
            timer = 0                         # timer를 0으로 설정
    button_green_old_value = button_green_value

    calc_time()                               # calc_time 함수 호출
    # minute, sec 변수를 00:00 형식으로 문자열 생성
    timer_str = "{:02d}:{:02d}".format(minute, sec)
    oled.setLine(2, timer_str)                # OLED 두 번째 줄에 timer_str 출력

    # 노랑 버튼을 눌렀다 뗀 상태라면
    if button_yellow_value == 0 and button_yellow_old_value == 1:
        start_timer()                         # start_timer 함수 호출

    oled.display()


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