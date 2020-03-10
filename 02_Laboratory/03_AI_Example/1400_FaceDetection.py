import sensor
import image
import lcd
import KPU as kpu

lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

print("load model...")
task = kpu.load("/sd/model/face.kmodel")
print("done...!")

anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)

a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

while(True):
    img = sensor.snapshot()
    code = kpu.run_yolo2(task, img)
    print(code)
    if code:
        for i in code:
            print(i)
            a = img.draw_rectangle(i.rect(),color = (0,0,255))
    a = lcd.display(img)
a = kpu.deinit(task)
