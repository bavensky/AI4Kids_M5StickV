# Lab 6 : Take a Photo to SD Card
# By: Apirak - apiruk326@gmail.com

import sensor, image, lcd, os
from Maix import I2S, GPIO
from fpioa_manager import fm
from board import board_info

# Register Button
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)

# Setup Button Mode
button_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
button_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

cnt_save = 0
cnt_show = 0

img_read = image.Image()

print(os.listdir())

try:
    while True:
        img = sensor.snapshot()
        lcd.display(img)

        # Take Photos
        if button_a.value() == 0:
            cnt_save+=1
            fname = "/sd/photos/"+str(cnt_save)+".jpg"
            print(fname)

            img.save(fname, quality=95)

        # Display Photos on Screen
        if button_b.value() == 0:
            cnt_show+=1
            img_read = image.Image("/sd/photos/"+str(cnt_show)+".jpg")
            lcd.display(img_read)
            print("Show Image " + str(cnt_show))
            time.sleep(1)
except:
    sys.exit()
