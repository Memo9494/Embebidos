import network
import urequests
from machine import Pin
from time import sleep
import dht

class SensorDHT:
    def __init__(self, ssid, password):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(ssid, password)
        while not self.wlan.isconnected():
            pass

        self.URL = "https://retoequipo1-3f172-default-rtdb.firebaseio.com/Reto_Equipo1/.json"
        self.URL_hora = "https://retoequipo1-3f172-default-rtdb.firebaseio.com/Reto_Equipo1/hora.json"
        self.sensor = dht.DHT11(Pin(14))

    def tempa(self, horas):
        return 22 + 1.32 * horas

    def tempb(self, horas):
        return 38 - 1.32 * horas

    def horas_map(self, horas):
        return {
            6:0, 7:1, 8:2, 9:3, 10:4, 11:5, 12:6, 13:7,
            14:8, 15:9, 16:10, 17:11, 18:12, 19:13,
            20:14, 21:15, 22:16, 23:17, 0:18, 1:19,
            2:20, 3:21, 4:22, 5:23
        }[horas]

    def get_temperature(self):
        try:
            sleep(2)
            self.sensor.measure()
            temp = self.sensor.temperature()
            temp_real_data = "{\"temp_real\":\"" + str(temp) + "\"}"
            temp_real = urequests.patch(self.URL, data=temp_real_data)
            res_real = temp_real.json()
            return res_real
        except OSError as e:
            print('Failed to read sensor.')
            return None

    def update_estimated_temperature(self):
        try:
            response = urequests.get(self.URL_hora)
            data = response.json()
            print(data.type)
            hora = data
            hora = self.horas_map(hora)
            if hora < 12:
                temp_est = self.tempa(hora)
            else:
                temp_est = self.tempb(hora)
            temp_est_data = "{\"temp_est\":\"" + str(temp_est) + "\"}"
            temp_est = urequests.patch(self.URL, data=temp_est_data)
            res_est = temp_est.json()
            return res_est
        except Exception as e:
            print(f"Error al obtener datos de temperatura estimada: {str(e)}")
            return None
