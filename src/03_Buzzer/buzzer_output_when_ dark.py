import machine
from time import localtime, sleep
from machine import Pin, ADC, SoftI2C
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *

import time


oled = oled_u8g2()
sensor = ADC(Pin(A1))
buzzer = Pin(D6)


def buzzer_output():
    CDS_Value = sensor.read()
    
    if CDS_Value < 1500:
        for i in range(80) :
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)
   
def display_clock():
    oled.clear()
    
    oled.setLine(1, "Digital Clock")
    
    now = time.localtime()
    time_str = "{:02d}:{:02d}".format(now[3], now[4])
    oled.setLine(2, time_str)
    
    oled.display()


def setup():
    sensor.atten(ADC.ATTN_11DB)
    buzzer.init(Pin.OUT)


def loop():
    display_clock()
    buzzer_output()

    time.sleep(1)


if __name__ == "__main__":
    setup()
    while True:
        loop()