# ******************************************************************************************
# FileName     : burglar_alarm.py
# Description  : 도난 경보기 만들어 보기
# Author       : 박은정
# Created Date : 2023.9.12
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정 
# ******************************************************************************************


# import
import machine
import time
import neopixel
from machine import Pin, ADC
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A1))                          # 조도 센서의 핀을 A1으로 지정
buzzer = Pin(D6)                               # 부저의 핀을 D6로 지정
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12)   # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)                # 조도 센서를 입력 모드로 설정
    buzzer.init(Pin.OUT)                       # 부저를 출력 모드로 설정


# loop
def loop():
    CDS_Value = sensor.read()                  # 조도 센서 값 저장

    if CDS_Value < 1500:                       # 조도 센서의 값이 1500 미만이라면
        for i in range(12):
            np[i] = (255, 0, 0)                # 네오픽셀[i]의 색상을 빨강으로 설정
        np.write()                             # 네오픽셀 출력

        for i in range(80) :                   # 부저에서 소리를 출력
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)

    time.sleep(1)


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