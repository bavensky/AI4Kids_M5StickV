# Lab 4 : Button
# By: Apirak - apiruk326@gmail.com

import sensor, time

from Maix import GPIO
from fpioa_manager import *
from board import board_info

# Register Button
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)

# Setup Button Mode
button_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
button_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

# Register LED
fm.register(board_info.LED_W, fm.fpioa.GPIO3)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)

# Setup LED Mode
led_w = GPIO(GPIO.GPIO3, GPIO.OUT)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

# LED is Active Low (0 is ON, 1 is OFF)
led_w.value(1) 
led_r.value(1) 
led_g.value(1)
led_b.value(1)

while(True):
    if button_a.value() == 0 and button_b.value() == 0:
        time.sleep_ms(200)
        print("Button A and B Press")
        led_r.value(0)
        led_g.value(1)
        led_b.value(1)
    elif button_a.value() == 0:
        time.sleep_ms(200)
        print("Button A Press")
        led_r.value(1)
        led_g.value(0)
        led_b.value(1)
    elif button_b.value() == 0:
        time.sleep_ms(200)
        print("Button B Press")
        led_r.value(1)
        led_g.value(1)
        led_b.value(0)