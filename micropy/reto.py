import machine
import ssd1306
from draw import Drawer

class Reto():
    def __init__(self):#, texto):


        #self.texto = texto

        i2c = machine.SoftI2C(scl=machine.Pin(18), sda=machine.Pin(19))
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)

        # oled.text(texto, 100, 0)
        # oled.show()
        drawer=Drawer(oled)
        drawer.draw_ellipse(55,40,10,20)
        drawer.draw_ellipse(64,32,10,2)
        drawer.draw_ellipse(50,60,2,5)
        drawer.draw_ellipse(60,60,2,5)
        drawer.draw_ellipse(40,40,5,10)



        


