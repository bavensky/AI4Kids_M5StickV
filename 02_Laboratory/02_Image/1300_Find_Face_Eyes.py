import video, sensor, image, lcd, time

lcd.init()
lcd.rotation(2)
# Reset sensor
sensor.reset()

# Sensor settings
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.RGB565)
sensor.run(1)
sensor.skip_frames(30)

# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.

face_cascade = image.HaarCascade("frontalface", stages=25)
eyes_cascade = image.HaarCascade("eye", stages=24)
tim = time.ticks_ms()

while True:
    # Capture snapshot
    img = sensor.snapshot()

    objects = img.find_features(face_cascade, threshold=0.5, scale_factor=1.5)
    for face in objects:
        print(face)
        img.draw_rectangle(face, color = (255, 0, 0))
        eyes = img.find_features(eyes_cascade, threshold=0.5, scale_factor=1.2, roi=face)
        for e in eyes:
            img.draw_rectangle(e, color = (0, 0, 255))
    lcd.display(img)
print("finish")
#v.record_finish()
lcd.clear()
