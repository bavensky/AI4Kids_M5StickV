import sensor
import image
import lcd
import time

lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)


#thresholds = (30, 100, 15, 127, 15, 127)    # RED
thresholds = (30, 100, -64, -8, -32, 32)    # GREEN
#thresholds = (0, 30, 0, 64, -128, 0)        # BLUE


while True:
    img = sensor.snapshot()
    blobs = img.find_blobs([thresholds])
    if blobs:
        for b in blobs:
            print(b)
            img = img.draw_rectangle(b[0:4])
            img = img.draw_cross(b[5], b[6])
    lcd.display(img)
