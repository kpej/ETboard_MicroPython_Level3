#*******************************************************************************************
# FileName     : 09._neopixel_tree.py
# Description  : 네오픽셀로 크리스마스 트리 만들어 보기
# Author       : 박은정
# Created Date : 2023.11.23
# Reference    :
# Modified     : 2023.11.28 : PEJ : 주석 수정
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
import neopixel


# global variable
num_pixels = 12
np = neopixel.NeoPixel(Pin(D2, Pin.OUT), num_pixels) # 네오픽셀의 핀을 D2로 지정하고 12개의 LED를 초기화


# setup
def setup():                                         # pass를 사용하여 건너뜀
    pass


# wheel
def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos*3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r,g,b)


# rainbow_cycle
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            np[i] = wheel(pixel_index & 255)
        np.write()
        time.sleep(wait)


# loop
def loop():
    rainbow_cycle(0.01)


# start point
if __name__ == '__main__':
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
