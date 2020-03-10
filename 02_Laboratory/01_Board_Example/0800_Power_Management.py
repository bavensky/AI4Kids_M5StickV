import pmu,lcd

lcd.init()
lcd.rotation(2)
lcd.clear()

axp = pmu.axp192()
axp.enableADCs(True)

while True:
    vbat = axp.getVbatVoltage()
    usb_vol = axp.getUSBVoltage()
    usb_cur = axp.getUSBInputCurrent()
    connext_vol = axp.getConnextVoltage()
    connext_input_current = axp.getConnextInputCurrent()
    bat_current= axp.getBatteryChargeCurrent()
    bat_dis_current = axp.getBatteryDischargeCurrent()
    bat_instant_watts = axp.getBatteryInstantWatts()
    temp = axp.getTemperature()

    lcd.draw_string(20,0,"usb_vol:"+str(usb_vol)+"mV : "+str(usb_vol/1000)+"V")
    lcd.draw_string(20,15,"usb_cur:"+str(usb_cur)+"mA")
    lcd.draw_string(20,30,"connext_vol:"+str(connext_vol)+"mV")
    lcd.draw_string(20,45,"connext_input_current:"+str(connext_input_current))
    lcd.draw_string(20,60,"bat_current:"+str(bat_current))
    lcd.draw_string(20,75,"bat_dis_current:"+str(bat_dis_current))
    lcd.draw_string(20,90,"bat_instant_watts:"+str(bat_instant_watts))
    lcd.draw_string(20,105,"temp:"+str(temp))
