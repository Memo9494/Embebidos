from SensorDHT import SensorDHT  # Asegúrate de que el archivo se llama mi_modulo.py
import time
from time import sleep
import ssd1306
sensor = SensorDHT("Xiaomi 12", "memo121255")

while True:
    real_temperature = sensor.get_temperature()
    estimated_temperature = sensor.update_estimated_temperature()
    if real_temperature is not None:
        print("Temperatura Real:", real_temperature)
    if estimated_temperature is not None:
        print("Temperatura Estimada:", estimated_temperature)
    sensor.oled.poweron()
    sensor.oled.text("temp real "+real_temperature,0,0)
    sensor.oled.text("temp estim "+estimated_temperature,0,20)
    sensor.oled.show()
    
    sleep(3)