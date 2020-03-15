from machine import I2C
import lcd

lcd.init()
lcd.rotation(2)
lcd.clear()

from Maix import GPIO
from fpioa_manager import *
from board import board_info

# Add Register
fm.register(board_info.LED_W, fm.fpioa.GPIO3)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)

# Setup LED Mode
led_w = GPIO(GPIO.GPIO3, GPIO.OUT)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

# LED is Active Low (0 is ON, 1 is OFF)
led_w.value(1)
led_r.value(1)
led_g.value(1)
led_b.value(1)

MPU6886_ADDRESS             =   0x68
MPU6886_WHOAMI              =   0x75
MPU6886_ACCEL_INTEL_CTRL    =  0x69
MPU6886_SMPLRT_DIV          =  0x19
MPU6886_INT_PIN_CFG         =  0x37
MPU6886_INT_ENABLE          =  0x38
MPU6886_ACCEL_XOUT_H        =  0x3B
MPU6886_TEMP_OUT_H          =  0x41
MPU6886_GYRO_XOUT_H         =  0x43
MPU6886_USER_CTRL           =  0x6A
MPU6886_PWR_MGMT_1          =  0x6B
MPU6886_PWR_MGMT_2          =  0x6C
MPU6886_CONFIG              =  0x1A
MPU6886_GYRO_CONFIG         =  0x1B
MPU6886_ACCEL_CONFIG        =  0x1C
MPU6886_ACCEL_CONFIG2       =  0x1D
MPU6886_FIFO_EN             =  0x23

i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29)
devices = i2c.scan()
time.sleep_ms(10)

print("i2c",devices)

def write_i2c(address, value):
    i2c.writeto_mem(MPU6886_ADDRESS, address, bytearray([value]))
    time.sleep_ms(10)

def MPU6886_init():
    write_i2c(MPU6886_PWR_MGMT_1, 0x00)
    write_i2c(MPU6886_PWR_MGMT_1, 0x01<<7)
    write_i2c(MPU6886_PWR_MGMT_1,0x01<<0)
    write_i2c(MPU6886_ACCEL_CONFIG,0x10)
    write_i2c(MPU6886_GYRO_CONFIG,0x18)
    write_i2c(MPU6886_CONFIG,0x01)
    write_i2c(MPU6886_SMPLRT_DIV,0x05)
    write_i2c(MPU6886_INT_ENABLE,0x00)
    write_i2c(MPU6886_ACCEL_CONFIG2,0x00)
    write_i2c(MPU6886_USER_CTRL,0x00)
    write_i2c(MPU6886_FIFO_EN,0x00)
    write_i2c(MPU6886_INT_PIN_CFG,0x22)
    write_i2c(MPU6886_INT_ENABLE,0x01)

def MPU6886_read():
    accel = i2c.readfrom_mem(MPU6886_ADDRESS, MPU6886_ACCEL_XOUT_H, 6)
    accel_x = (accel[0]<<8|accel[1])
    accel_y = (accel[2]<<8|accel[3])
    accel_z = (accel[4]<<8|accel[5])
    if accel_x>32768:
        accel_x=accel_x-65536
    if accel_y>32768:
        accel_y=accel_y-65536
    if accel_z>32768:
        accel_z=accel_z-65536
    return accel_x,accel_y,accel_z

MPU6886_init()

#Possible accelerometer scales (and their register bit settings) are:
#2 Gs (00), 4 Gs (01), 8 Gs (10), and 16 Gs  (11).

#aRes = 2.0 / 32768.0;
#aRes = 4.0 / 32768.0;
aRes = 8.0/32768.0;
#aRes = 16.0 / 32768.0;

while True:
    x,y,z = MPU6886_read()
    accel_array = [x*aRes, y*aRes, z*aRes]
    print(accel_array)

    lcd.draw_string(10,10,"Gyro & Acc MPU6886")
    lcd.draw_string(20,50,"x:"+str(accel_array[0]))
    lcd.draw_string(20,70,"y:"+str(accel_array[1]))
    lcd.draw_string(20,90,"z:"+str(accel_array[2]))

    if accel_array[1] > 0.8:
        led_w.value(0)
    else:
        led_w.value(1)

    time.sleep_ms(1000)
