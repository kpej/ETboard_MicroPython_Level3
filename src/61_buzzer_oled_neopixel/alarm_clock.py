# ******************************************************************************************
# FileName     : alarm_clock.py
# Description  : 알람시계 만들어 보기
# Author       : 박은정
# Created Date : 2023.9.19
# Reference    :
# Modified     : 2023.11.29 : PEJ : 주석 수정 
# ******************************************************************************************


# import
import machine
import neopixel
import time
from machine import Pin, ADC
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *


# global variable
oled = oled_u8g2()                            # OLED 선언

buzzer = Pin(D6)                              # 부저의 핀을 D6로 지정

button_yellow = Pin(D9)                       # 노랑 버튼의 핀을 D9로 지정
button_blue = Pin(D7)                         # 파랑 버튼의 핀을 D7로 지정
button_green = Pin(D8)                        # 초록 버튼의 핀을 D8로 지정

pir = Pin(D3)                                 # 인체 감지 센서의 핀을 D3로 지정

np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12)  # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화

button_blue_value = 0                         # 파랑 버튼의 상태
button_blue_old_value = 1                     # 파랑 버튼의 이전 상태

button_green_value = 0                        # 초록 버튼의 상태
button_green_old_value = 1                    # 초록 버튼의 이전 상태

button_yellow_value = 0                       # 노랑 버튼의 상태
button_yellow_old_value = 1                   # 노랑 버튼의 이전 상태

alarm_value = 1

hour = 0                                      # 시간을 저장
minute = 0                                    # 분을 저장


# setup
def setup():
    buzzer.init(Pin.OUT)

    button_yellow.init(Pin.IN)
    button_blue.init(Pin.IN)
    button_green.init(Pin.IN)

    pir = Pin(Pin.IN)


# alarm_setup : 알람을 설정하는 함수
def alarm_setup():
    # 전역변수 호출
    global hour, minute, /
    button_yellow_value, button_yellow_old_value, /
    button_blue_value, button_blue_old_value, /
    button_green_value, button_green_old_value

    # 노랑 버튼의 상태를 변수에 저장
    button_yellow_value = button_yellow.value()
    button_yellow_old_value = button_yellow_value

    while True:
        # 노랑, 파랑, 초록 버튼의 상태를 변수에 저장
        button_yellow_value = button_yellow.value()
        button_blue_value = button_blue.value()
        button_green_value = button_green.value()

        # 노랑 버튼을 눌렀다 뗀 상태라면
        if button_yellow_value == 0 and button_yellow_old_value == 1:
            break                             # while문을 종료
        button_yellow_old_value = button_yellow_value

        # 파랑 버튼을 눌렀다 뗀 상태라면
        if button_blue_value == 0 and button_blue_old_value == 1:
            hour = hour + 1                   # hour 변수에 1을 더함
        button_blue_old_value = button_blue_value
        
        if button_green_value == 0 and button_green_old_value == 1:
            minute = minute + 1               # minute 변수에 1을 더함
        button_green_old_value = button_green_value

        if minute > 59:                       # minute의 값이 59보다 크다면
            hour = hour + 1                   # hour 변수에 1을 더함
            minute = 0                        # minute의 값을 0으로 설정

       if hour > 24:                          # hour의 값이 24보다 크다면
            hour = 1                          # hour의 값을 1로 설정

        oled.clear()                          # OLED 초기화
        oled.setLine(1, "alram setup")        # OLED의 첫 줄에 "alram setup" 출력
        # hour과 minute 변수의 형식을 00:00으로 하여 변수에 저장
        time_str = "{:02d}:{:02d}".format(hour, minute)
        oled.setLine(2, time_str)             # OLED의 두 번째 줄에 time_str 값 출력

        oled.display()                        # OLED 출력


# alarm_action : 알람이 시작되면 작동하는 함수
def alarm_action():
    # 전역변수 호출
    global alarm_value, /
           button_green_value, button_green_old_value

    # 초록 버튼의 상태를 변수에 저장
    button_green_value = button_green.value()
    button_green_old_value = button_green_value

    oled.clear()                              # OLED 초기화
    
    oled.setLine(1, "alarm action")           # OLED의 첫 줄에 "alram action" 출력
    
    oled.display()                            # OLED 출력
    
    while True:
        # 초록 버튼의 상태를 변수에 저장
        button_green_value = button_green.value()
        
        if pir.value() == HIGH:               # 인체 감지 센서의 값이 HIGH라면
            for i in range(0, 12):
                np[i] = (255, 0, 0)           # 네오픽셀의 색상을 빨강으로 지정
                np.write()                    # 네오픽셀 출력
        else:                                 # 아니라면
            for i in range(0, 12):
                np[i] = (0, 0, 0)             # 네오픽셀의 색상을 초기화
                np.write()                    # 네오픽셀 출력

        # 초록 버튼을 눌렀다 뗸 상태라면
        if button_green_value == 0 and button_green_old_value == 1:
            alarm_value = 0
            for i in range(0, 12):
                np[i] = (0, 0, 0)             # 네오픽셀의 색상을 초기화
                np.write()                    # 네오픽셀 출력
            break                             # while문 종료
        button_green_old_value = button_green_value
        
        for i in range(80) :                  # 부저에서 소리를 재생
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)
        time.sleep(1)


# display_clock : OLED에 시간을 출력하는 함수
def display_clock():
    # 전역변수 호출
    global hour, minute, alarm_value
    
    oled.clear()                              # OLED 초기화
    
    now = time.localtime()                    # 현재 시간 저장
    # 현재 시간과 분을 00:00 형식으로 저장 =
    time_str = "{:02d}:{:02d}".format(now[3], now[4])

    if now[3] == 0 and now[4] == 0:           # 하루가 지나면 다시 알람 가동
        alarm_value = 1

    # 현재 시간과 분이 설정된 알람과 동일하며 alarm_value의 값이 1이라면
    if now[3] == hour and now[4] == minute and alarm_value == 1:
        alarm_action()                        # alarm_action 함수 호출

    oled.setLine(1, "Digital Clock")          # OLED의 첫 줄에 "Digital Clock" 출력
    oled.setLine(2, time_str)                 # OLED의 두 번째 줄에 time_str 값 출력
    
    oled.display()


# loop
def loop():
    # 전역변수 호출
    global button_yellow_value, button_yellow_old_value
    
    # 노랑 버튼의 상태를 변수에 저장
    button_yellow_value = button_yellow.value()

    display_clock()                           # display_clock 함수 호출

    # 노랑 버튼을 눌렀다 뗀 상태라면
    if button_yellow_value == 0 and button_yellow_old_value == 1:
        alarm_setup()                         # alarm_setup 함수 호출
    button_yellow_old_value = button_yellow_value


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