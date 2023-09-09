import network
import urequests
import machine
from machine import Pin, SoftI2C
from time import sleep
import dht
import ssd1306



class SensorDHT:
    
    def __init__(self, ssid, password):

        # Network
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(ssid, password)
        while not self.wlan.isconnected():
            pass

        self.URL = "https://retoequipo1-3f172-default-rtdb.firebaseio.com/Reto_Equipo1/.json"
        self.URL_hora = "https://retoequipo1-3f172-default-rtdb.firebaseio.com/Reto_Equipo1/hora.json"
        # Initialize LCD Display
        self.i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
        self.oled_width = 128
        self.oled_height = 64
        self.oled = ssd1306.SSD1306_I2C(self.oled_width,self.oled_height,self.i2c)

        


        # Initalize Sensor DHT11
        self.sensor = dht.DHT11(Pin(14))
    
    def lcd_str(self, message, col, row):
        self.lcd.move_to(col, row)
        self.lcd.putstr(message)

    def tempa(self, horas):
        return 22 + 1.32 * horas

    def tempb(self, horas):
        return 38 - 1.32 * horas

    def horas_map(self, horas):
        return {
            6:0, 7:1, 8:2, 9:3, 10:4, 11:5, 12:6, 13:7,
            14:8, 15:9, 16:10, 17:11, 18:12, 19:0,
            20:1, 21:2, 22:3, 23:4, 0:5, 1:6,
            2:7, 3:8, 4:9, 5:10
        }[horas]

    def get_temperature(self):
        try:
            sleep(2)
            self.sensor.measure()
            temp = self.sensor.temperature()
            temp_real_data = "{\"temp_real\":\"" + str(temp) + "\"}"
            temp_real = urequests.patch(self.URL, data=temp_real_data)
            res_real = temp_real.json()
            return str(temp)
        except OSError as e:
            print('Failed to read sensor.')
            return ""

    def update_estimated_temperature(self):
        try:
            response = urequests.get(self.URL_hora)
            data = response.json()
            print(data)
            hora = int(data)
            print(hora)
            if hora < 12:
                hora = self.horas_map(hora)
                temp_est = self.tempa(hora)
            else:
                hora = self.horas_map(hora)
                temp_est = self.tempb(hora)
            tempv = temp_est
            temp_est_data = "{\"temp_est\":\"" + str(temp_est) + "\"}"
            temp_est = urequests.patch(self.URL, data=temp_est_data)
            res_est = temp_est.json()
            return str(tempv)
        except Exception as e:
            print(f"Error al obtener datos de temperatura estimada: {str(e)}")
            return ""
