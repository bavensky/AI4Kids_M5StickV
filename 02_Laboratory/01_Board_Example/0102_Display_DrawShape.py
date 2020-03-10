# Lab 1-2 : Display Draw any Shape
# By: Apirak - apiruk326@gmail.com

import lcd
import image
import sensor

lcd.init(type=1, freq=15000000, color=lcd.WHITE)
lcd.rotation(2)
lcd.clear(lcd.BLACK)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

lcd.draw_string(0, 0, "M5StickV Capture & Draw Image")
time.sleep_ms(3000)

img = sensor.snapshot()

while True:
    img = img.draw_string(60, 60, "Draw Shape", scale=2)
    img = img.draw_line(50, 150, 240, 100, color = (255,255,0), thickness = 5)
    img = img.draw_arrow(70, 90, 170, 170, color = (0,0,255), thickness = 5)
    img = img.draw_circle(100, 150, 30, color = (255,0,0), thickness=3)
    img = img.draw_ellipse(220, 150, 30, 20, color = (0,255,0), thickness=3)
    lcd.display(img)


