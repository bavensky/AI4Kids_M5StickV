# Lab 1-1 : Display Draw String
# By: Apirak - apiruk326@gmail.com

import lcd
import image

lcd.init(type=1, freq=15000000, color=lcd.WHITE)
lcd.rotation(2)

while True:
    lcd.draw_string(0, 0, "M5Stick V 240x135 pixels", lcd.BLACK, lcd.WHITE)
    lcd.draw_string(0, 15, "Line 2")
    lcd.draw_string(0, 30, "Line 3")
    lcd.draw_string(0, 45, "Line 4")
    lcd.draw_string(0, 60, "Line 5")
    lcd.draw_string(0, 75, "Line 6")
    lcd.draw_string(0, 90, "Line 7")
    lcd.draw_string(0, 105, "Line 8")
