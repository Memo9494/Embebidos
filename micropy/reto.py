import machine
import ssd1306
import time
import max6675
import amogos

class Reto():
    def __init__(self):
        i2c = machine.SoftI2C(scl=machine.Pin(18), sda=machine.Pin(19))
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)

        while True:

            max = max6675.MAX6675(17, 16 , 27)

            print("Temperature: {}".format(max.readCelsius()))

            # Clear the OLED display
            oled.fill(0)
            oled.text("Mediciones: ", 0, 0)

            # Display the signal value on the OLED display
            oled.text("Temp: {}".format(max.readCelsius()), 0, 20)

            # Read and print analog value from pin 2
            # set pin 2 to analog input mode
            adc = machine.ADC(machine.Pin(2))
            oled.text("ADC: {}".format(adc.read()), 0, 30)
            print("ADC: {}".format(adc.read()))

            oled.show()
            # amogos.Amogos(oled, -30, 0)
            # amogos.Amogos(oled, 30, 0)
            time.sleep(1)
            

        
        
        

