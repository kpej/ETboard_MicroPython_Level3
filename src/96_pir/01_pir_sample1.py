# ********************************************************************************
# FileName : 01_pir_sample1.py
# Description : PIR(D9)센서 감지시 빨간LED(D2)를 깜밖이기
# Author : 손철수
# Created Date : 2023.09.19
# Reference : 한번 감지되면 5초동안 감지(HIGH) 신호 발생
#             D3, D9만 작동됨 ??
# Modified : 
# ********************************************************************************

# import
from ETboard.lib.pin_define import *
from machine import Pin
import time

# global definition


# setup
PinLED = Pin(D2, Pin.OUT)    # D2를 LED 출력모드 설정하기
PinLED.value(LOW)            # 빨강 LED 끄기

PinPiR = Pin(D9, Pin.IN)     # D6을 버튼 입력모드 설정하기


# main loop
while True:
    if PinPiR.value() == HIGH:
        PinLED.value(HIGH)        # 빨강 LED 켜기
        time.sleep(0.1)           # 0.1초 기다리기
        PinLED.value(LOW)         # 빨강 LED 켜기
        time.sleep(0.1)           # 0.1초 기다리기

# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr│
# │                                           │
# └───────────────────────────────────────────┘
