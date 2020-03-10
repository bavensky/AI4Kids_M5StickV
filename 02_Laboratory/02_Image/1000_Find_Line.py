# Lab 10 : Find Line
# By: Apirak - apiruk326@gmail.com

import sensor, image, lcd, time
lcd.init()
lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(30)

while True : 
    img  = sensor.snapshot () 
    lines  =  img.find_lines () 
       
    if lines:
        print (str(lines))
        print (str(lines[0][0]) + " to " + str(lines[0][1]))
        print (str(lines[0][2]) + " to " + str(lines[0][3]))
        for l in lines:
            img.draw_line(l.line(), color = (255, 0, 0))
            lcd.display(img)