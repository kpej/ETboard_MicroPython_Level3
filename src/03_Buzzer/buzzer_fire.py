import machine
from machine import Pin, ADC, SoftI2C
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *
import time
import neopixel


buzzer = Pin(D6)                    # 부저 핀 지정

sensor = ADC(Pin(A3))

np = neopixel.NeoPixel(Pin(D2, Pin.OUT), 12) # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화

def setup():
    buzzer.init(Pin.OUT)
    
    sensor.atten(ADC.ATTN_11DB)


def loop():
    sensor_value = sensor.read()
    
    for i in range(12):
        np[i] = (0, 0, 0)                      # 네오픽셀의 색상을 빨강으로 지정
        np.write()                               # 네오픽셀 출력

    if sensor_value < 50:
        for i in range(12):
            np[i] = (255, 0, 0)                      # 네오픽셀의 색상을 빨강으로 지정
            np.write()                               # 네오픽셀 출력
        
        for i in range(80) :             # 소리를 짧게 한번 냄
            buzzer.value(HIGH)
            time.sleep(0.001)
            buzzer.value(LOW)
            time.sleep(0.001)
        time.sleep(1)
        
if __name__ == "__main__":
    setup()
    while True:
        loop()