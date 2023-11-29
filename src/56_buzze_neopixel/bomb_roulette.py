# ******************************************************************************************
# FileName     : bomb_roulette
# Description  : 폭탄 룰렛 게임 만들어 보기
# Author       : 박은정
# Created Date : 2023.11.28
# Reference    :
# Modified     : 
# ******************************************************************************************


# import
import time
import neopixel
import random
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
buzzer = Pin(D5)                             # 부저의 핀을 D5로 지정

np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12) # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화

button_red = Pin(D6)                         # 빨강 버튼의 핀을 D6로 지정

button_red_value = 0                         # 빨강 버튼의 상태
button_red_old_value = 1                     # 빨강 버튼의 이전 상태

bomb_time = 0                                # 폭탄의 시간을 저장


# setup
def setup():
    buzzer.init(Pin.OUT)                     # 부저 출력 모드 설정
    button_red.init(Pin.IN)                  # 빨강 버튼 입력 모드 설정


# loop
def loop():
    # 전역 변수 호출
    global bomb_time, button_red_value, button_red_old_value

    button_red_value = button_red.value()    # 빨강 버튼의 값 저장

    for i in range(0, 12):
        np[i] = (0, 0, 0)                    # 네오픽셀의 색상을 초기화
    np.write()                               # 네오픽셀 출력

    # 빨강 버튼을 눌렀다 뗀 상태라면
    if button_red_value == 0 and button_red_old_value == 1:
        bomb_time = random.randint(5, 30)    # 5 이상 30 이하의 랜덤 숫자 생성

        while bomb_time > 0:                 # bomb_time이 0 이상이면 반복
            bomb_time = bomb_time - 1        # bomb_time을 1초 감소
            
            for i in range(80):              # 부저에서 소리를 재생
                buzzer.value(HIGH)
                time.sleep(0.001)
                buzzer.value(LOW)
                time.sleep(0.001)
            time.sleep(1)
        
        for i in range(0, 12):
            np[i] = (255, 0, 0)              # 네오픽셀의 색상을 빨강으로 지정
        np.write()                           # 네오픽셀 출력
        
        for i in range(5):                   # 부저에서 5초간 소리를 재생
            for j in range(5):
                for x in range(80):
                    buzzer.value(HIGH)
                    time.sleep(0.001)
                    buzzer.value(LOW)
                    time.sleep(0.001)
                time.sleep(0.01)
            time.sleep(0.5)

    button_red_old_value = button_red_value


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