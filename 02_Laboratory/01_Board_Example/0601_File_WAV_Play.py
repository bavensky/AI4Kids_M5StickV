# Lab 6-1 : Play WAV song from SD Card
# By: Apirak - apiruk326@gmail.com

import sensor, lcd, sys

from Maix import I2S, GPIO
import audio
from Maix import GPIO
from fpioa_manager import *

# Register Speaker
fm.register(board_info.SPK_SD, fm.fpioa.GPIO0)
spk_sd=GPIO(GPIO.GPIO0, GPIO.OUT)
spk_sd.value(1) #Enable the SPK output

fm.register(board_info.SPK_DIN,fm.fpioa.I2S0_OUT_D1)
fm.register(board_info.SPK_BCLK,fm.fpioa.I2S0_SCLK)
fm.register(board_info.SPK_LRCLK,fm.fpioa.I2S0_WS)

wav_dev = I2S(I2S.DEVICE_0)

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

def play_sound(filename):
    try:
        player = audio.Audio(path = filename)
        player.volume(100)
        wav_info = player.play_process(wav_dev)
        wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER,resolution = I2S.RESOLUTION_16_BIT, align_mode = I2S.STANDARD_MODE)
        wav_dev.set_sample_rate(wav_info[1])
        while True:
            ret = player.play()
            if ret == None:
                break
            elif ret==0:
                break
        player.finish()
    except:
        pass


try:
    while True:
        lcd.draw_string(5, 5, "Play WAV from SD Card", lcd.WHITE, lcd.BLACK)
        lcd.draw_string(80, 60, "Press Button A -->", lcd.WHITE, lcd.BLACK)
        if button_a.value() == 0:
            play_sound("/sd/wav/super_mario.wav")
            print("Play WAV song")
            time.sleep(1)
except:
    sys.exit()
