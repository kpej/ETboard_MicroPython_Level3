import machine
from machine import Pin, ADC, SoftI2C
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *

import time

oled = oled_u8g2()

buzzer = Pin(D6)                    # 부저 핀 지정

button_blue = Pin(D7)                         # 파랑 버튼 핀 지정
button_green = Pin(D8)                        # 초록 버튼 핀 지정

button_yellow = Pin(D9)                          # 빨강 버튼 핀 지정
button_blue = Pin(D7)                         # 파랑 버튼 핀 지정
button_green = Pin(D8)                        # 초록 버튼 핀 지정

button_yellow_value = 0                          # 빨강 버튼의 상태
button_yellow_old_value = 1                      # 빨강 버튼의 이전 상태

button_blue_value = 0                         # 파랑 버튼의 상태
button_blue_old_value = 1                     # 파랑 버튼의 이전 상태

button_green_value = 0                        # 초록 버튼의 상태
button_green_old_value = 1                    # 초록 버튼의 이전 상태

sec = 0


def start_timer():
    global sec
    
    timer = sec
    
    oled.clear()
    oled.setLine(1, "timer start!")
    oled.setLine(2, str(timer) + " sec")
    
    oled.display()
    
    for i in range(0, sec):
        timer = timer - 1
        
        oled.clear()
        
        oled.setLine(1, "timer start!")
        oled.setLine(2, str(timer) + " sec")
        
        oled.display()
        
        time.sleep(1)
           
    buzzer.value(HIGH)
        
    for i in range(5):
        for j in range(80):
            button_yellow_value = button_yellow.value()
            
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)
        time.sleep(1)

    sec = 0


def setup():
    buzzer.init(Pin.OUT)
    
    button_yellow.init(Pin.IN)                   # 빨강 버튼 입력모드 설정하기
    button_blue.init(Pin.IN)                  # 파랑 버튼 입력모드 설정하기
    button_green.init(Pin.IN)                 # 초록 버튼 입력모드 설정하기


def loop():
    global sec, button_blue_value, button_blue_old_value, button_green_value, button_green_old_value, button_yellow_value, button_yellow_old_value

    button_yellow_value = button_yellow.value()
    button_blue_value = button_blue.value()
    button_green_value = button_green.value()
    
    oled.clear()
    
    oled.setLine(1, "set timer!")
    oled.setLine(2, str(sec) + " sec") 
    
    if button_blue_value == 0 and button_blue_old_value == 1:
        sec = sec + 5
        oled.setLine(2, str(sec) + " sec")
    button_blue_old_value = button_blue_value
    
    if button_green_value == 0 and button_green_old_value == 1:
        sec = sec - 5
        
        if sec < 0:
            sec = 0
        
        oled.setLine(2, str(sec) + " sec")
    button_green_old_value = button_green_value
    
    if button_yellow_value == 0 and button_yellow_old_value == 1:
        start_timer()
    
    oled.display()
    

if __name__ == "__main__":
    setup()
    while True:
        loop()