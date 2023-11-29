# ******************************************************************************************
# FileName     : fire_alarm.py
# Description  : 화재경보기 만들어 보기
# Author       : 박은정
# Created Date : 2023.9.25
# Reference    :
# Modified     : 2023.11.21 : PEJ : 주석 들여쓰기 수정
# Modified     : 2023.11.28 : PEJ : 주석 수정 
# ******************************************************************************************


# import
import machine
import time
import neopixel
from machine import Pin, ADC
from ETboard.lib.pin_define import *


# global variable
buzzer = Pin(D6)                                 # 부저의 핀을 D6 지정

sensor = ADC(Pin(A3))                            # 불꽃 감지 센서의 핀을 A3로 지정

np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12)     # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화


# setup
def setup():
    buzzer.init(Pin.OUT)                         # 부저를 출력 모드로 설정
    sensor.atten(ADC.ATTN_11DB)                  # 불꽃 감지 센서를 입력 모드로 설정


# loop
def loop():
    sensor_value = sensor.read()                 # 불꽃 감지 센서의 값을 젖아

    for i in range(12):
        np[i] = (0, 0, 0)                        # 네오픽셀의 색상을 초기화
        np.write()                               # 네오픽셀 출력
        
    print(sensor_value)

    if sensor_value < 50:                        # 불꽃 감지 센서의 값이 50 미만이라면
        for i in range(12):
            np[i] = (255, 0, 0)                  # 네오픽셀의 색상을 빨강으로 지정
            np.write()                           # 네오픽셀 출력

        for i in range(80) :                     # 부저에서 소리를 재생
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