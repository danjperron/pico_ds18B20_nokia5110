import machine, onewire, ds18x20, utime
import lcd5110

# define nokia LCD display
lcd = lcd5110.LCD5110()

# define DS18B20 onewire
ds_pin = machine.Pin(18)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# scan sensors
sensorsID = ds_sensor.scan()


lcd.text("DS18B20",10,0,1)
lcd.text("-DEMO-",10,10,1)
lcd.text("#1",0,20,1)
lcd.text("#2",0,30,1)

# Boucle infinie
while True:

    # DS18B20 conversion
    ds_sensor.convert_temp()

    for ID in sensorsID:
        idx = sensorsID.index(ID)+1
        info = "{:.1f}'C ".format(ds_sensor.read_temp(ID))
        # display info
        lcd.fill_rect(30,10+idx*10,lcd.WIDTH-1,19+idx*10,0)
        lcd.text(info,30,10+idx*10,1,True)
    
    utime.sleep(1)
