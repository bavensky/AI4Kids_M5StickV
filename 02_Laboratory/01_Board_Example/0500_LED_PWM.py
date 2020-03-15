# Lab 5 : PWM (Pulse Width Modulation)
# By: Apirak - apiruk326@gmail.com

import sensor,time,math
from fpioa_manager import *

from Maix import GPIO
from board import board_info
from machine import Timer,PWM

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


# PWM Pin
pwm_led1 = board_info.LED_R
pwm_led2 = board_info.LED_G

pwm1 = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
PWM_ch1 = PWM(pwm1, freq=500000, duty=0, pin=pwm_led1)

pwm2 = Timer(Timer.TIMER1, Timer.CHANNEL1, mode=Timer.MODE_PWM)
PWM_ch2 = PWM(pwm2, freq=500000, duty=0, pin=pwm_led2)

duty_val = 100


led_w.value(1)
led_r.value(1)
led_g.value(1)
led_b.value(1)

try:
    while(True):
        # PWM Value 0 is ON and 100 is OFF
        for duty_val in range(100, 0, -1):
              PWM_ch1.duty(duty_val)
            time.sleep_ms(10)
        for duty_val in range(0, 100, 1):
            PWM_ch1.duty(duty_val)
            time.sleep_ms(10)

        for duty_val in range(100, 0, -1):
            PWM_ch2.duty(duty_val)
            time.sleep_ms(10)
        for duty_val in range(0, 100, 1):
            PWM_ch2.duty(duty_val)
            time.sleep_ms(10)
except:
    fm.unregister(board_info.LED_W, fm.fpioa.GPIO3)
    fm.unregister(board_info.LED_R, fm.fpioa.GPIO4)
    fm.unregister(board_info.LED_G, fm.fpioa.GPIO5)
    fm.unregister(board_info.LED_B, fm.fpioa.GPIO6)
