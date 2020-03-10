#find circles
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
    for c in img.find_circles(threshold = 3500, x_margin = 10, y_margin = 10, r_margin = 10, r_min = 2, r_max = 100, r_step = 2,roi=(80,60,160,120)):
        img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
    img.draw_rectangle(80,60,160,120)
    lcd.display(img)

print("finish")
lcd.clear()
