"""
File runs on boot, it is the first script that executes
Empty for now
"""

# import network
# sta_if = network.WLAN(network.STA_IF)
# if not sta_if.isconnected():
#     print('connecting to network...')
#     sta_if.active(True)
#     sta_if.connect('Extreme BS', '')
#     while not sta_if.isconnected():
#         pass
# print('network config:', sta_if.ifconfig())
import machine
import ssd1306
import amogos

i2c = machine.SoftI2C(scl=machine.Pin(12), sda=machine.Pin(14))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
amogos.Amogos()
#print amogos
oled.fill(0)
oled.text("Amogos", 0, 0)

oled.show()
