# Lab 2 : Live Stream
# By: Apirak - apiruk326@gmail.com

import lcd
import image
import sensor

lcd.init()
lcd.rotation(2)


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

lcd.draw_string(40, 60, "M5StickV Live Stream", lcd.WHITE, lcd.BLACK)
time.sleep_ms(3000)


while True:
    img = sensor.snapshot()
    img.draw_string(60, 60, "Live Stream", color = (255,0,0), scale=2)
    lcd.display(img)
