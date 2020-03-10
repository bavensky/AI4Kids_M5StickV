import sensor,image,lcd,time
import KPU as kpu

from Maix import GPIO
from fpioa_manager import *
from board import board_info

lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_hmirror(0)
sensor.set_vflip(0)
sensor.run(1)

fm.register(board_info.LED_R, fm.fpioa.GPIO4)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_r.value(1)

clock = time.clock()

classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
task = kpu.load("/sd/model/20class.kmodel")
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

try:
    while(True):
        clock.tick()
        img = sensor.snapshot()
        code = kpu.run_yolo2(task, img)
        #print(clock.fps())

        if code:
            for i in code:
                a = img.draw_rectangle(i.rect())
                a = lcd.display(img)
                for i in code:
                    print(i.classid())
                    if i.classid() == 7:
                        led_r.value(0)
                    else:
                        led_r.value(1)

                    lcd.draw_string(i.x(), i.y(), classes[i.classid()], lcd.RED, lcd.WHITE)
                    lcd.draw_string(i.x(), i.y()+12, '%f1.3'%i.value(), lcd.RED, lcd.WHITE)
        else:
            a = lcd.display(img)
except:
    a = kpu.deinit(task)
    sys.exit()
