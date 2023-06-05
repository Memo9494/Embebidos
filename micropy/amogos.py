import machine
import ssd1306
from draw import Drawer

class Amogos():
    def __init__(self, oled, x0 = 0, y0 = 0):#, texto):
        drawer=Drawer(oled)
        drawer.draw_ellipse(55 + x0, 40 + y0, 10, 20)
        drawer.draw_ellipse(64 + x0, 32 + y0, 10, 2)
        drawer.draw_ellipse(50 + x0, 60 + y0, 2, 5)
        drawer.draw_ellipse(60 + x0, 60 + y0, 2, 5)
        drawer.draw_ellipse(40 + x0, 40 + y0, 5, 10)



        


