#find rects
import video, sensor, image, lcd, time

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(30)

while True:
    img = sensor.snapshot()
    for r in img.find_rects(threshold = 18000,roi=(80,60,160,120)):
        img.draw_rectangle(r.rect(), color = (255, 0, 0))
        for p in r.corners(): img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
    img.draw_rectangle(80,60,160,120)

    lcd.display(img)

print("finish")
lcd.clear()
