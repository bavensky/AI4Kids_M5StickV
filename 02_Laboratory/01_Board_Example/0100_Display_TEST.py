# Lab 1 : Display Test
# By: Apirak - apiruk326@gmail.com

import lcd
import time

lcd.init()

lcd.clear(lcd.RED)
time.sleep_ms(1000)

lcd.clear(lcd.GREEN)
time.sleep_ms(1000)

lcd.clear(lcd.BLUE)
time.sleep_ms(1000)

lcd.clear(lcd.YELLOW)
time.sleep_ms(1000)

lcd.clear(lcd.WHITE)
time.sleep_ms(1000)

lcd.clear(lcd.BLACK)
time.sleep_ms(1000)

while True:
    lcd.rotation(2)
    lcd.draw_string(0, 0, "Hello World!")
    lcd.draw_string(0, 15, "M5 Stick V")
    lcd.draw_string(0, 30, "LCD Display 135x240")
