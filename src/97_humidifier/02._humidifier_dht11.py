# ******************************************************************************************
# FileName     : 01_humidfier_dht11_oled.py
# Description  : 버튼으로 가습기  제어하기
# Author       : 손철수
# Created Date : 2023.09.17
# Reference    :
# Modified     : 
# ******************************************************************************************

# import
import time
from machine import Pin
from ETboard.lib.pin_define import *
import dht
from ETboard.lib.OLED_U8G2 import *

# global variable
led_red = Pin(D2)                              # 빨강 LED 핀 지정
led_blue = Pin(D3)                             # 파랑 LED 핀 지정
button_red = Pin(D6)                           # 빨강 버튼 핀 지정
button_blue = Pin(D7)                          # 파랑 버튼 핀 지정
button_green = Pin(D8)                         # 녹색 버튼 핀 지정

sensor = dht.DHT11(Pin(D9))                    # 온습도(DHT11) 센서 핀 지정
oled = oled_u8g2()

# setup
def setup() :
    led_red.init(Pin.OUT)                      # 빨강 LED 출력모드 설정
    led_blue.init(Pin.OUT)                     # 파랑 LED 출력모드 설정
    button_red.init(Pin.IN)                    # 빨강 버튼 입력모드 설정하기
    button_blue.init(Pin.IN)                   # 파랑 버튼 입력모드 설정하기
    button_green.init(Pin.IN)                  # 녹색 버튼 입력모드 설정하기
    
    stop_humidifier()                          # 초기 상태에는 가습기를 정지시키기
    
# main loop
def loop() :
    
    # 버튼 상태 저장하기
    button_red_value = button_red.value()
    button_blue_value = button_blue.value()
    button_green_value = button_green.value()
    
    # 빨강 버튼으로 가습기 작동시키기
    if button_red_value == 0:
        run_humidifier()
        time.sleep(0.3)
        
    # 파랑 버튼으로 가습기 멈추기    
    if button_blue_value == 0:
        stop_humidifier()
        time.sleep(0.3)
        
    # 녹색 버튼으로 가습기 10초 작동시키기    
    if button_green_value == 0:
        run_humidifier()
        time.sleep(10)
        stop_humidifier()
        
    sensor.measure()                  # 온습도 센서 값 측정
    print(sensor.temperature(),       # 온도 값 출력
          sensor.humidity())          # 습도 값 출력
    oled.setLine(1, 'DHT11 sensor')   # OLED 모듈 1번 줄에 저장
    oled.setLine(2, 'temp: ' + str(sensor.temperature()) + 'c')    # OLED 모듈 2번 줄에 저장
    oled.setLine(3, 'humi: ' + str(sensor.humidity()) + '%')       # OLED 모듈 3번 줄에 저장
    oled.display()                    # 저장된 내용을 oled 에 보여줌
    time.sleep(1)       
    
    
# run_humidifier    
def run_humidifier():
    led_red.value(HIGH)                        # 빨강 LED 켜기
    led_blue.value(LOW)                        # 파랑 LED 끄기

# run_humidifier
def stop_humidifier():
    led_red.value(LOW)                         # 빨강 LED 끄기
    led_blue.value(LOW)                        # 파랑 LED 끄기    


if __name__ == "__main__" :
    setup()
    while True :
        loop()
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
