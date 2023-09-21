import machine
from machine import Pin, ADC, SoftI2C
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *

import time

oled = oled_u8g2()

buzzer = Pin(D6)                    # 부저 핀 지정

button_yellow = Pin(D9)                       # 노랑 버튼 핀 지정
button_blue = Pin(D7)                         # 파랑 버튼 핀 지정
button_green = Pin(D8)                        # 초록 버튼 핀 지정

button_blue_value = 0                         # 파랑 버튼의 상태
button_blue_old_value = 1                     # 파랑 버튼의 이전 상태

button_green_value = 0                        # 초록 버튼의 상태
button_green_old_value = 1                    # 초록 버튼의 이전 상태

button_yellow_value = 0                       # 노랑 버튼의 상태
button_yellow_old_value = 1                   # 노랑 버튼의 이전 상태

alram_time = 0

local_time = time.localtime()
month = local_time[1]
day = local_time[2]

hour = 0
minute = 0


def alarm_setup():
    global alram_time, month, day, hour, minute
    global button_yellow_value, button_yellow_old_value
    global button_blue_value, button_blue_old_value
    global button_green_value, button_green_old_value

    button_yellow_value = button_yellow.value()
    button_yellow_old_value = button_yellow_value
    
    now = time.localtime()
    month = now[1]
    day = now[2]

    while True:
        button_yellow_value = button_yellow.value()
        button_blue_value = button_blue.value()
        button_green_value = button_green.value()
        
        if button_yellow_value == 0 and button_yellow_old_value == 1:
            break        
        button_yellow_old_value = button_yellow_value

        oled.clear()
        oled.setLine(1, "alram setup")
        time_str = "{:02d}:{:02d}".format(hour, minute)
        oled.setLine(2, time_str)

        if button_blue_value == 0 and button_blue_old_value == 1:
            hour = hour + 1
            if hour > 24:
                hour = 1
        button_blue_old_value = button_blue_value
        
        if button_green_value == 0 and button_green_old_value == 1:
            minute = minute + 1
            if minute > 59:
                hour = hour + 1
                minute = 0
        button_green_old_value = button_green_value

        oled.display()
    
def alarm_action():
    oled.clear()
    
    oled.setLine(1, "alarm action")
    
    oled.display()
    
    for i in range(10):    
        button_yellow_old_value = button_yellow_value
        
        for j in range(80) :
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)
        time.sleep(1)

def alarm_day_control():
    global month, day

    day = day + 1

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31:
            month + 1
            day = 1
    else:
        if day > 30:
            month + 1
            day = 1
    
    if month > 13:
        month = 1


def display_clock():
    global month, day
    
    oled.clear()
    
    oled.setLine(1, "Digital Clock")
    
    now = time.localtime()
    time_str = "{:02d}:{:02d}".format(now[3], now[4])
    
    if now[1] == month and now[2] == day and now[3] == hour and now[4] == minute:
        alarm_action()
        alarm_day_control()
        oled.setLine(1, "Digital Clock")

    oled.setLine(2, time_str)
    
    oled.display()


def setup():
    buzzer.init(Pin.OUT)
    
    button_yellow.init(Pin.IN)
    button_blue.init(Pin.IN)
    button_green.init(Pin.IN)


def loop():
    global alram_time, button_yellow_value, button_yellow_old_value

    button_yellow_value = button_yellow.value()
    
    display_clock()

    
    if button_yellow_value == 0 and button_yellow_old_value == 1:
        alarm_setup()

    button_yellow_old_value = button_yellow_value

if __name__ == "__main__":
    setup()
    while True:
        loop()